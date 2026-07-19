#!/usr/bin/env python3
"""Validate structural consistency in the Aetherbound campaign repository.

Uses only the Python standard library. Run from the repository root:

    python scripts/validate_repository.py

Exit codes:
    0: no errors (warnings may be present)
    1: one or more validation errors
    2: no errors, but warnings exist and --strict-warnings was supplied
"""

from __future__ import annotations

import argparse
import csv
import fnmatch
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Iterator, Sequence
from urllib.parse import unquote

EXPECTED_KNOWN_DEAD_ZONE_COUNT = 10
EXPECTED_HIDDEN_DEAD_ZONE_COUNT = 8
EXPECTED_ACTUAL_DEAD_ZONE_COUNT = 18
DEAD_ZONE_MANIFEST = Path("validation/dead_zones.json")
WORLD_BIBLE_PATH = Path("canon/DnD_Campaign_World_Bible.md")
GEOGRAPHY_PATH = Path("canon/World_Geography.md")
CITY_PROFILE_GLOB = "cities/*_City_Profile.md"
NPC_MASTER_PATH = Path("npcs/NPC_Backstory_Personality_file.md")
STAT_BLOCK_PATH = Path("combat/Enemy_Encounters_Stat_Blocks.md")
CREATURE_ROOT = Path("creatures")
CREATURE_MANIFEST = CREATURE_ROOT / "manifest.json"
CREATURE_DATA_JSON = CREATURE_ROOT / "data/creatures.json"
CREATURE_DATA_CSV = CREATURE_ROOT / "data/creatures.csv"
CREATURE_INDEX = CREATURE_ROOT / "Creature_Catalog_Index.md"
ROLL_ROOT = CREATURE_ROOT / "roll_tables"
ROLL_MANIFEST = ROLL_ROOT / "manifest.json"
ROLL_DATA_JSON = ROLL_ROOT / "data/roll_tables.json"
ROLL_DATA_CSV = ROLL_ROOT / "data/roll_tables.csv"
EXPECTED_CREATURE_COUNT = 161
EXPECTED_CREATURE_CATEGORY_COUNT = 23
EXPECTED_CREATURE_GROUP_COUNT = 4
EXPECTED_ROLL_TABLE_COUNT = 23
EXPECTED_ROLL_RESULT_COUNT = 138
EXPECTED_GATE_INVASION_RESULT_COUNT = 24

EXPECTED_MAJOR_CITY_COUNT = 15
EXPECTED_MINOR_CITY_COUNT = 20
EXPECTED_TOTAL_CITY_COUNT = 35
EXPECTED_GATE_CITY_COUNT = 3
EXPECTED_FEATURED_CITY_PROFILES = {
    "Ravensport",
    "Deepanvil",
    "Faerindel",
    "Ironforge",
}

REQUIRED_CITY_HEADINGS = {
    "city identity",
    "leadership",
    "districts",
    "key locations and proprietors",
    "basic services",
    "trade and supply",
    "daily life and current tensions",
    "defenses",
    "immediate plot hooks",
}

REQUIRED_STAT_FIELDS = {
    "cr": re.compile(r"\*\*CR:\*\*", re.I),
    "encounter role": re.compile(r"\*\*Encounter Role:\*\*", re.I),
    "ac": re.compile(r"\*\*AC:\*\*", re.I),
    "hp": re.compile(r"\*\*HP:\*\*", re.I),
    "speed": re.compile(r"\*\*Speed:\*\*", re.I),
    "attacks": re.compile(r"^\*\*Attacks\*\*\s*$", re.I | re.M),
    "abilities": re.compile(r"^\*\*Abilities\*\*\s*$", re.I | re.M),
    "tactics": re.compile(r"^\*\*Tactics\*\*\s*$", re.I | re.M),
    "dead-zone variant": re.compile(
        r"^\*\*Dead-Zone / Anti-Magic Variant\*\*\s*$", re.I | re.M
    ),
}

FORBIDDEN_PLACEHOLDER_PATTERNS = {
    "TBD": re.compile(r"\bTBD\b", re.I),
    "TODO": re.compile(r"\bTODO\b", re.I),
    "FIXME": re.compile(r"\bFIXME\b", re.I),
    "XXX": re.compile(r"\bXXX\b", re.I),
    "PLACEHOLDER": re.compile(r"\bPLACEHOLDER\b"),
    "INSERT marker": re.compile(r"\bINSERT\s+(?:TEXT|CONTENT|HERE)\b", re.I),
    "template braces": re.compile(r"\{\{[^{}\n]+\}\}"),
    "placeholder brackets": re.compile(
        r"\[\[(?:TODO|TBD|PLACEHOLDER)[^\]\n]*\]\]", re.I
    ),
    "lorem ipsum": re.compile(r"\bLorem\s+ipsum\b", re.I),
}

TITLE_PREFIXES = re.compile(
    r"^(?:lord protector|gate warden|master of trade|archmage|captain|gate commander|"
    r"high warden|archdruidess|master enchanter|trade envoy|lorekeeper|high thane|"
    r"master engineer|forge mistress|chief engineer|master miner|forge overseer|"
    r"security captain|trade factor|head engineer|innkeeper|barkeep|apothecary|"
    r"weaver|enchanter|trader|jeweler|weaponsmith|master armorer|fence)\s+",
    re.I,
)

FILE_TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9_])([A-Za-z0-9_./*()\-]+\.(?:md|png|py|ya?ml|json))(?![A-Za-z0-9_])",
    re.I,
)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)


@dataclass(frozen=True)
class Finding:
    severity: str
    check: str
    message: str
    file: str | None = None
    line: int | None = None


class Validator:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.findings: list[Finding] = []
        self._texts: dict[Path, str] = {}
        self._metadata: dict[Path, dict[str, str]] = {}

    def add(
        self,
        severity: str,
        check: str,
        message: str,
        path: Path | None = None,
        line: int | None = None,
    ) -> None:
        rel = None
        if path is not None:
            try:
                rel = path.resolve().relative_to(self.root).as_posix()
            except ValueError:
                rel = str(path)
        self.findings.append(Finding(severity, check, message, rel, line))

    def error(self, check: str, message: str, path: Path | None = None, line: int | None = None) -> None:
        self.add("ERROR", check, message, path, line)

    def warn(self, check: str, message: str, path: Path | None = None, line: int | None = None) -> None:
        self.add("WARN", check, message, path, line)

    def pass_(self, check: str, message: str) -> None:
        self.add("PASS", check, message)

    def text(self, path: Path) -> str:
        if path not in self._texts:
            self._texts[path] = path.read_text(encoding="utf-8")
        return self._texts[path]

    def metadata(self, path: Path) -> dict[str, str]:
        if path not in self._metadata:
            self._metadata[path] = parse_front_matter(self.text(path))
        return self._metadata[path]

    def markdown_files(self) -> list[Path]:
        return sorted(
            p
            for p in self.root.rglob("*.md")
            if ".git" not in p.parts and not any(part.startswith(".") and part != ".github" for part in p.parts)
        )

    def active_markdown_files(self) -> list[Path]:
        active: list[Path] = []
        for path in self.markdown_files():
            status = self.metadata(path).get("status", "")
            if status.casefold() not in {"historical", "superseded"}:
                active.append(path)
        return active

    def run(self) -> None:
        self.check_internal_references()
        self.check_forbidden_placeholders()
        self.check_counts()
        self.check_city_headings()
        self.check_stat_blocks()
        self.check_index_metadata()
        self.check_canonical_ownership()
        self.check_pending_inventory()
        self.check_creature_catalog()
        self.check_roll_tables()

    # ------------------------------------------------------------------
    # Internal filenames and links
    # ------------------------------------------------------------------
    def check_internal_references(self) -> None:
        check = "internal references"
        examined = 0
        missing = 0
        bad_anchors = 0

        for path in self.active_markdown_files():
            text = self.text(path)
            strict = True
            scan_text = active_pending_text(text) if path.name == "Pending_Changes.md" else text
            declared_new_refs: set[str] = set()
            if path.name == "Pending_Changes.md":
                for pending_line in scan_text.splitlines():
                    if re.search(r"\b(?:new file|at implementation|create)\b", pending_line, re.I):
                        declared_new_refs.update(FILE_TOKEN_RE.findall(pending_line))

            refs: list[tuple[str, int, str | None]] = []
            for match in MARKDOWN_LINK_RE.finditer(scan_text):
                raw = match.group(1).strip()
                refs.append((raw, line_number(scan_text, match.start(1)), "link"))
            for match in FILE_TOKEN_RE.finditer(scan_text):
                refs.append((match.group(1), line_number(scan_text, match.start(1)), "token"))

            seen: set[tuple[str, int]] = set()
            for raw, line, kind in refs:
                key = (raw, line)
                if key in seen:
                    continue
                seen.add(key)
                examined += 1

                candidate_raw = raw.strip("()<>`")
                if candidate_raw in {
                    "Exact_File_Name.md", "*_City_Profile.md", "Pending_Changes_Archived_XX.md",
                    "history/Pending_Changes_Archived_XX.md",
                    "validation-results.json", "validation-output.txt", "validation-report.json",
                }:
                    continue
                if raw.startswith(("http://", "https://", "mailto:")):
                    continue

                target_raw = unquote(candidate_raw.strip("*"))
                anchor: str | None = None
                if "#" in target_raw:
                    target_raw, anchor = target_raw.split("#", 1)

                if not target_raw:
                    target = path
                else:
                    target = (path.parent / target_raw).resolve()

                exists = False
                matched_paths: list[Path] = []
                if any(char in target_raw for char in "*?["):
                    pattern = target_raw
                    matched_paths = [p for p in path.parent.glob(pattern) if p.is_file()]
                    if not matched_paths and kind == "token":
                        matched_paths = [p for p in self.root.glob(pattern) if p.is_file()]
                    exists = bool(matched_paths)
                else:
                    exists = target.is_file()
                    if exists:
                        matched_paths = [target]
                    elif kind == "token":
                        root_target = (self.root / target_raw).resolve()
                        if root_target.is_file():
                            target = root_target
                            matched_paths = [root_target]
                            exists = True

                if not exists:
                    if path.name == "Pending_Changes.md" and raw in declared_new_refs:
                        continue
                    missing += 1
                    message = f"Referenced path does not exist: {raw}"
                    self.error(check, message, path, line)
                    continue

                if anchor and kind == "link" and len(matched_paths) == 1 and matched_paths[0].suffix.lower() == ".md":
                    anchors = markdown_anchors(self.text(matched_paths[0]))
                    if anchor.casefold() not in anchors:
                        bad_anchors += 1
                        message = f"Anchor '#{anchor}' was not found in {target_raw or path.name}"
                        self.error(check, message, path, line)

        if missing == 0 and bad_anchors == 0:
            self.pass_(check, f"Verified {examined} internal filename/link references.")

    # ------------------------------------------------------------------
    # Forbidden placeholders
    # ------------------------------------------------------------------
    def check_forbidden_placeholders(self) -> None:
        check = "forbidden placeholders"
        hits = 0
        for path in self.active_markdown_files():
            text = self.text(path)
            if path.name == "Pending_Changes.md":
                text = active_pending_text(text)
            text = strip_code(text)

            for label, pattern in FORBIDDEN_PLACEHOLDER_PATTERNS.items():
                for match in pattern.finditer(text):
                    hits += 1
                    self.error(
                        check,
                        f"Forbidden placeholder marker '{label}': {match.group(0)!r}",
                        path,
                        line_number(text, match.start()),
                    )
        if hits == 0:
            self.pass_(check, "No forbidden placeholder markers were found in active Markdown.")

    # ------------------------------------------------------------------
    # Dead-zone and city counts
    # ------------------------------------------------------------------
    def check_counts(self) -> None:
        check = "dead-zone and city counts"
        world = self.root / WORLD_BIBLE_PATH
        geography = self.root / GEOGRAPHY_PATH
        index = self.root / "Campaign_Index_and_Quick_Reference.md"
        manifest_path = self.root / DEAD_ZONE_MANIFEST
        if not world.is_file() or not geography.is_file() or not index.is_file():
            self.error(check, "World Bible, Geography, or Campaign Index is missing.")
            return
        if not manifest_path.is_file():
            self.error(check, f"Dead-zone manifest is missing: {DEAD_ZONE_MANIFEST.as_posix()}")
            return

        world_text = self.text(world)
        geo_text = self.text(geography)
        index_text = self.text(index)

        major_section = section_between(world_text, r"^### Major Cities \(15 total\)", r"^### Minor / Sub-Cities")
        minor_section = section_between(world_text, r"^### Minor / Sub-Cities \(20 total\)", r"^## 6\.")
        major = extract_city_bullets(major_section)
        minor = extract_city_bullets(minor_section)
        all_world = major + minor

        self._check_expected_unique_count(check, "major cities", major, EXPECTED_MAJOR_CITY_COUNT, world)
        self._check_expected_unique_count(check, "minor cities", minor, EXPECTED_MINOR_CITY_COUNT, world)
        self._check_expected_unique_count(check, "total cities", all_world, EXPECTED_TOTAL_CITY_COUNT, world)

        gate_section = section_between(world_text, r"^### The Three Gate Cities", r"^### Gate-City Security")
        gate_cities = re.findall(r"^\|\s*\*\*([^*]+)\*\*\s*\|", gate_section, re.M)
        self._check_expected_unique_count(check, "gate cities", gate_cities, EXPECTED_GATE_CITY_COUNT, world)

        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.error(check, f"Dead-zone manifest could not be read: {exc}", manifest_path)
            return

        counts = manifest.get("counts", {})
        expected_counts = {
            "known": EXPECTED_KNOWN_DEAD_ZONE_COUNT,
            "hidden": EXPECTED_HIDDEN_DEAD_ZONE_COUNT,
            "actual": EXPECTED_ACTUAL_DEAD_ZONE_COUNT,
        }
        for label, expected in expected_counts.items():
            if counts.get(label) != expected:
                self.error(check, f"Manifest {label} dead-zone count must be {expected}; found {counts.get(label)!r}.", manifest_path)

        zones = manifest.get("zones", [])
        if not isinstance(zones, list):
            self.error(check, "Manifest zones value must be a list.", manifest_path)
            zones = []
        ids = [str(zone.get("id", "")).strip() for zone in zones if isinstance(zone, dict)]
        if len(zones) != EXPECTED_ACTUAL_DEAD_ZONE_COUNT:
            self.error(check, f"Manifest must contain {EXPECTED_ACTUAL_DEAD_ZONE_COUNT} physical zones; found {len(zones)}.", manifest_path)
        duplicate_ids = sorted(name for name, count in Counter(ids).items() if name and count > 1)
        if duplicate_ids or any(not value for value in ids):
            self.error(check, f"Manifest dead-zone IDs must be nonempty and unique; duplicates: {duplicate_ids}.", manifest_path)

        known_zones = [zone for zone in zones if isinstance(zone, dict) and zone.get("known") is True]
        hidden_zones = [zone for zone in zones if isinstance(zone, dict) and zone.get("known") is False]
        if len(known_zones) != EXPECTED_KNOWN_DEAD_ZONE_COUNT:
            self.error(check, f"Manifest must mark {EXPECTED_KNOWN_DEAD_ZONE_COUNT} zones as known; found {len(known_zones)}.", manifest_path)
        if len(hidden_zones) != EXPECTED_HIDDEN_DEAD_ZONE_COUNT:
            self.error(check, f"Manifest must mark {EXPECTED_HIDDEN_DEAD_ZONE_COUNT} zones as hidden; found {len(hidden_zones)}.", manifest_path)
        if any(not zone.get("public_name") for zone in known_zones):
            self.error(check, "Every known dead-zone manifest entry requires a public_name.", manifest_path)
        if any(zone.get("public_name") not in {None, ""} for zone in hidden_zones):
            self.error(check, "Hidden dead-zone manifest entries must not have public names.", manifest_path)

        map_info = manifest.get("map", {})
        map_rel = map_info.get("path", "")
        map_file = self.root / map_rel if map_rel else None
        if not map_file or not map_file.is_file():
            self.error(check, f"Manifest map file does not exist: {map_rel!r}.", manifest_path)
        else:
            actual_sha = hashlib.sha256(map_file.read_bytes()).hexdigest()
            expected_sha = map_info.get("sha256", "")
            if actual_sha != expected_sha:
                self.error(check, "Canonical map checksum changed; perform a new visual dead-zone audit before updating the manifest.", map_file)
        if map_info.get("public_legend_count") != EXPECTED_KNOWN_DEAD_ZONE_COUNT:
            self.error(check, f"Map public legend count must remain {EXPECTED_KNOWN_DEAD_ZONE_COUNT} until in-world knowledge changes.", manifest_path)

        dz_section = section_between(geo_text, r"^## 7\. Magic Dead Zones", r"^## 8\.")
        known_section = section_between(dz_section, r"^### Publicly Known and Recorded Zones", r"^### DM-Only: Eight Unrecorded Dead Zones")
        dz_rows = re.findall(r"^\|\s*(\d+)\s*\|\s*\*\*([^*]+)\*\*\s*\|", known_section, re.M)
        dz_numbers = [int(n) for n, _ in dz_rows]
        dz_names = [name.strip() for _, name in dz_rows]
        self._check_expected_unique_count(check, "known dead zones", dz_names, EXPECTED_KNOWN_DEAD_ZONE_COUNT, geography)
        if dz_numbers != list(range(1, EXPECTED_KNOWN_DEAD_ZONE_COUNT + 1)):
            self.error(check, f"Known dead-zone numbering must be 1-{EXPECTED_KNOWN_DEAD_ZONE_COUNT}; found {dz_numbers}.", geography)

        manifest_names = {normalize_name(str(zone.get("public_name"))) for zone in known_zones}
        geography_names = {normalize_name(name) for name in dz_names}
        if manifest_names != geography_names:
            self.error(check, f"Known dead-zone names differ between Geography and manifest: geography={sorted(geography_names)}, manifest={sorted(manifest_names)}.", geography)

        hidden_section = section_between(dz_section, r"^### DM-Only: Eight Unrecorded Dead Zones", r"^### Dead-Zone Route Effects")
        hidden_ids = re.findall(r"^\|\s*(H-\d{2})\s*\|", hidden_section, re.M)
        manifest_hidden_ids = {str(zone.get("id")) for zone in hidden_zones}
        if len(hidden_ids) != EXPECTED_HIDDEN_DEAD_ZONE_COUNT or set(hidden_ids) != manifest_hidden_ids:
            self.error(check, f"Geography hidden-zone IDs must match the {EXPECTED_HIDDEN_DEAD_ZONE_COUNT} manifest entries; found {hidden_ids}.", geography)

        required_authority_phrases = [
            (world, world_text, r"DM-only reality:\*\* Elyndria physically contains \*\*18 magic dead zones"),
            (geography, geo_text, r"10 Known, 8 Hidden"),
            (index, index_text, r"ten publicly known dead zones and eight hidden dead zones"),
        ]
        for path, source, pattern in required_authority_phrases:
            if not re.search(pattern, source, re.I):
                self.error(check, "Required known-versus-hidden dead-zone statement is missing.", path)

        obsolete_patterns = [
            r"exactly ten dead zones",
            r"magic dead zones — exactly 10",
            r"the ten dead zones are produced",
        ]
        for path, source in [(world, world_text), (geography, geo_text), (index, index_text)]:
            for pattern in obsolete_patterns:
                match = re.search(pattern, source, re.I)
                if match:
                    self.error(check, f"Obsolete physical-count wording remains: {match.group(0)!r}.", path, line_number(source, match.start()))

        allowed_hidden_files = {
            world.resolve(), geography.resolve(), index.resolve(),
            (self.root / "VALIDATION.md").resolve(),
        }
        hidden_reveal = re.compile(r"(?:18|eighteen)\s+(?:physical\s+)?(?:magic\s+)?dead zones|8\s+(?:additional\s+)?hidden dead zones", re.I)
        for active_path in self.active_markdown_files():
            if active_path.resolve() in allowed_hidden_files:
                continue
            source = strip_code(self.text(active_path))
            match = hidden_reveal.search(source)
            if match:
                self.error(check, "DM-only full dead-zone count is exposed outside an approved authority or validation file.", active_path, line_number(source, match.start()))

        geo_city_section = section_between(geo_text, r"^## 5\. Settlement Placement", r"^## 6\.")
        geo_cities: list[str] = []
        for start_heading, end_heading in [
            (r"^### Major Elven Cities", r"^### Major Dwarven Cities"),
            (r"^### Major Dwarven Cities", r"^### Major Human-Influenced or Mixed Cities"),
            (r"^### Major Human-Influenced or Mixed Cities", r"^### Elven Minor Cities"),
            (r"^### Elven Minor Cities", r"^### Dwarven Minor Cities"),
            (r"^### Dwarven Minor Cities", r"^### Mixed Minor Cities"),
            (r"^### Mixed Minor Cities", r"^### Map-Marked Local Settlements and Outposts"),
        ]:
            category = section_between(geo_city_section, start_heading, end_heading)
            geo_cities.extend(re.findall(r"^\|\s*\*\*([^*]+)\*\*\s*\|", category, re.M))
        self._check_expected_unique_count(check, "geography city entries", geo_cities, EXPECTED_TOTAL_CITY_COUNT, geography)

        world_set = {normalize_name(x) for x in all_world}
        geo_set = {normalize_name(x) for x in geo_cities}
        if world_set != geo_set:
            missing_geo = sorted(world_set - geo_set)
            extra_geo = sorted(geo_set - world_set)
            if missing_geo:
                self.error(check, f"Cities present in World Bible but missing from Geography: {missing_geo}", geography)
            if extra_geo:
                self.error(check, f"Cities present in Geography but absent from World Bible: {extra_geo}", geography)

        profile_names: list[str] = []
        for profile in sorted(self.root.glob(CITY_PROFILE_GLOB)):
            match = re.search(r"^#\s+(.+?)\s+City Profile\s*$", self.text(profile), re.M)
            if match:
                profile_names.append(match.group(1).strip())
            else:
                self.error(check, "City profile lacks a '# <City> City Profile' heading.", profile)
        if set(profile_names) != EXPECTED_FEATURED_CITY_PROFILES:
            self.error(check, "Featured city profiles do not match expected set: " f"expected {sorted(EXPECTED_FEATURED_CITY_PROFILES)}, found {sorted(profile_names)}.")

        if not any(f.severity == "ERROR" and f.check == check for f in self.findings):
            self.pass_(check, "Verified 10 known, 8 hidden, and 18 physical dead zones; 15 major cities, 20 minor cities, 35 total cities, 3 gate cities, and 4 featured city profiles.")

    def _check_expected_unique_count(
        self, check: str, label: str, values: Sequence[str], expected: int, path: Path
    ) -> None:
        normalized = [normalize_name(v) for v in values]
        duplicates = sorted(name for name, count in Counter(normalized).items() if count > 1)
        if len(values) != expected:
            self.error(check, f"Expected {expected} {label}; found {len(values)}.", path)
        if duplicates:
            self.error(check, f"Duplicate {label}: {duplicates}", path)

    # ------------------------------------------------------------------
    # City headings
    # ------------------------------------------------------------------
    def check_city_headings(self) -> None:
        check = "mandatory city headings"
        profiles = sorted(self.root.glob(CITY_PROFILE_GLOB))
        if not profiles:
            self.error(check, "No city profile files were found.")
            return

        for path in profiles:
            headings = {
                normalize_heading(title)
                for hashes, title in HEADING_RE.findall(self.text(path))
                if len(hashes) == 2
            }
            missing = sorted(REQUIRED_CITY_HEADINGS - headings)
            if missing:
                self.error(check, f"Missing mandatory H2 headings: {missing}", path)
            if not any("interaction" in heading for heading in headings):
                self.error(
                    check,
                    "Missing mandatory interaction heading covering gates, dead zones, or cultures.",
                    path,
                )
        if not any(f.severity == "ERROR" and f.check == check for f in self.findings):
            self.pass_(check, f"All {len(profiles)} city profiles contain the mandatory headings.")

    # ------------------------------------------------------------------
    # Actionable stat blocks
    # ------------------------------------------------------------------
    def check_stat_blocks(self) -> None:
        check = "actionable stat blocks"
        path = self.root / STAT_BLOCK_PATH
        if not path.is_file():
            self.error(check, f"Stat-block repository is missing: {STAT_BLOCK_PATH.as_posix()}.")
            return

        blocks = split_h2_sections(self.text(path))
        actionable = [(name, body, line) for name, body, line in blocks if re.search(r"\*\*CR:\*\*", body, re.I)]
        if not actionable:
            self.error(check, "No CR-bearing stat blocks were found.", path)
            return

        names = [normalize_name(name) for name, _, _ in actionable]
        duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
        if duplicates:
            self.error(check, f"Duplicate stat-block headings: {duplicates}", path)

        for name, body, line in actionable:
            for field, pattern in REQUIRED_STAT_FIELDS.items():
                if not pattern.search(body):
                    self.error(check, f"'{name}' is missing required field: {field}.", path, line)

            attacks_match = re.search(
                r"^\*\*Attacks\*\*\s*$([\s\S]*?)(?=^\*\*[A-Z][^\n]*\*\*\s*$|\Z)",
                body,
                re.I | re.M,
            )
            attacks = attacks_match.group(1) if attacks_match else ""
            has_attack_bonus = bool(re.search(r"[+-]\d+\s+to hit", attacks, re.I))
            has_damage = bool(re.search(r"\b\d+\s*\(\d+d\d+(?:\s*[+-]\s*\d+)?\)", attacks, re.I))
            if not has_attack_bonus:
                self.error(check, f"'{name}' has no attack entry with a to-hit bonus.", path, line)
            if not has_damage:
                self.error(check, f"'{name}' has no attack entry with average and dice damage.", path, line)

        if not any(f.severity == "ERROR" and f.check == check for f in self.findings):
            self.pass_(check, f"All {len(actionable)} CR-bearing stat blocks are actionable.")

    # ------------------------------------------------------------------
    # Index versions/status vs metadata
    # ------------------------------------------------------------------
    def check_index_metadata(self) -> None:
        check = "Index metadata comparison"
        index = self.root / "Campaign_Index_and_Quick_Reference.md"
        if not index.is_file():
            self.error(check, "Campaign Index is missing.")
            return

        rows = parse_index_file_rows(self.text(index))
        if not rows:
            self.error(check, "No parseable file inventory rows were found in the Campaign Index.", index)
            return

        indexed_paths: set[Path] = set()
        for filename, row in rows.items():
            if any(char in filename for char in "*?["):
                if not list(self.root.glob(filename)):
                    self.error(check, f"Index wildcard matches no files: {filename}", index, row["line"])
                continue

            target = self.root / filename
            if target.suffix.lower() == ".md":
                indexed_paths.add(target.resolve())
            if not target.is_file():
                self.error(check, f"Index lists a missing file: {filename}", index, row["line"])
                continue

            if target.suffix.lower() != ".md" or target.name == "README.md":
                continue
            meta = self.metadata(target)
            if not meta:
                self.error(check, f"Indexed file has no front-matter metadata: {filename}", target)
                continue

            version = row.get("version", "").strip()
            status = row.get("metadata status", row.get("status", "")).strip()
            if not version:
                self.error(check, f"Index row lacks a Version value for {filename}.", index, row["line"])
            elif version != meta.get("version", ""):
                self.error(
                    check,
                    f"Index version for {filename} is {version!r}; file metadata is {meta.get('version', '')!r}.",
                    index,
                    row["line"],
                )
            if not status:
                self.error(check, f"Index row lacks a Metadata status value for {filename}.", index, row["line"])
            elif normalize_name(status) != normalize_name(meta.get("status", "")):
                self.error(
                    check,
                    f"Index status for {filename} is {status!r}; file metadata is {meta.get('status', '')!r}.",
                    index,
                    row["line"],
                )

        required_index_files = {
            p.resolve()
            for p in self.active_markdown_files()
            if self.metadata(p)
            and p.name not in {"README.md"}
            and not p.name.startswith("Pending_Changes_Archived_")
        }
        missing_rows = sorted(
            p.relative_to(self.root).as_posix()
            for p in required_index_files - indexed_paths
        )
        if missing_rows:
            self.error(check, f"Metadata-bearing active files missing from Index inventory: {missing_rows}", index)

        if not any(f.severity == "ERROR" and f.check == check for f in self.findings):
            self.pass_(check, f"Index version/status values match {len(indexed_paths)} active files.")

    # ------------------------------------------------------------------
    # Duplicate canonical NPC/location ownership
    # ------------------------------------------------------------------
    def check_canonical_ownership(self) -> None:
        check = "canonical ownership"
        active_files = self.active_markdown_files()

        authority_owners: dict[str, list[Path]] = defaultdict(list)
        for path in active_files:
            authority = self.metadata(path).get("authority")
            if authority:
                authority_owners[normalize_name(authority)].append(path)
        for authority, owners in authority_owners.items():
            if len(owners) > 1:
                self.error(
                    check,
                    f"Authority label is claimed by multiple active files: {authority}: "
                    f"{[p.relative_to(self.root).as_posix() for p in owners]}",
                )

        npc_file = self.root / NPC_MASTER_PATH
        if not npc_file.is_file():
            self.error(check, f"NPC master file is missing: {NPC_MASTER_PATH.as_posix()}.")
            return
        npc_headings = [title for hashes, title in HEADING_RE.findall(self.text(npc_file)) if len(hashes) == 3]
        npc_names = [canonical_npc_name(title) for title in npc_headings]
        npc_dupes = sorted(name for name, count in Counter(npc_names).items() if count > 1)
        if npc_dupes:
            self.error(check, f"Duplicate canonical NPC entries in master file: {npc_dupes}", npc_file)
        npc_set = set(npc_names)

        profile_city_owners: dict[str, list[Path]] = defaultdict(list)
        location_owners: dict[str, list[tuple[Path, str]]] = defaultdict(list)
        proprietor_locations: dict[str, list[tuple[Path, str]]] = defaultdict(list)

        for profile in sorted(self.root.glob(CITY_PROFILE_GLOB)):
            title_match = re.search(r"^#\s+(.+?)\s+City Profile\s*$", self.text(profile), re.M)
            if title_match:
                profile_city_owners[normalize_name(title_match.group(1))].append(profile)

            key_section = section_between(
                self.text(profile), r"^## Key Locations and Proprietors", r"^## Basic Services"
            )
            proprietor_section = section_between(
                key_section, r"^### Inns and Taverns", r"^### Recurring Contacts|^## "
            )
            for raw_name, raw_owner in extract_location_owner_entries(proprietor_section):
                location = normalize_name(raw_name)
                owner = canonical_npc_name(raw_owner) if raw_owner else ""
                location_owners[location].append((profile, owner))
                if owner:
                    proprietor_locations[owner].append((profile, raw_name))
                    if owner not in npc_set:
                        self.error(
                            check,
                            f"Proprietor '{raw_owner}' for '{raw_name}' has no canonical NPC master entry.",
                            profile,
                        )

            if "NPC_Backstory_Personality_file.md" not in key_section:
                self.warn(
                    check,
                    "City profile does not explicitly point full NPC profiles to NPC_Backstory_Personality_file.md.",
                    profile,
                )

        for city, owners in profile_city_owners.items():
            if len(owners) > 1:
                self.error(
                    check,
                    f"City '{city}' has multiple canonical city-profile owners: "
                    f"{[p.name for p in owners]}",
                )
        for location, owners in location_owners.items():
            unique_profiles = {p for p, _ in owners}
            if len(unique_profiles) > 1:
                self.error(
                    check,
                    f"Location '{location}' is canonically defined in multiple city profiles: "
                    f"{[p.name for p in unique_profiles]}",
                )
        for proprietor, entries in proprietor_locations.items():
            unique_locations = {normalize_name(loc) for _, loc in entries}
            if len(unique_locations) > 1:
                self.error(
                    check,
                    f"Proprietor '{proprietor}' owns multiple named locations: {sorted(unique_locations)}.",
                )

        if not any(f.severity == "ERROR" and f.check == check for f in self.findings):
            self.pass_(
                check,
                f"Verified unique authority claims, {len(npc_names)} canonical NPC entries, "
                f"{len(profile_city_owners)} city-profile owners, and {len(location_owners)} named locations.",
            )

    # ------------------------------------------------------------------
    # Pending inventory vs repository files
    # ------------------------------------------------------------------
    def check_pending_inventory(self) -> None:
        check = "Pending inventory"
        pending = self.root / "Pending_Changes.md"
        if not pending.is_file():
            self.error(check, "Pending_Changes.md is missing.")
            return

        text = active_pending_text(self.text(pending))
        no_active = bool(re.search(r"_No active proposals\._", text, re.I))
        headings = re.findall(r"^###\s+(.+)$", text, re.M)
        refs = [m.group(1) for m in FILE_TOKEN_RE.finditer(text) if m.group(1) != "Exact_File_Name.md"]

        if no_active:
            if headings or refs:
                self.error(check, "Pending file says no active proposals but still contains proposal headings or file inventory.", pending)
            else:
                self.pass_(check, "Pending inventory is empty and consistent with the active template.")
            return

        if not headings:
            self.error(check, "Active Pending content has no proposal heading.", pending)

        missing: list[str] = []
        declared_new: list[str] = []
        existing: list[str] = []
        lines = text.splitlines()
        for ref in sorted(set(refs)):
            matches = list(self.root.glob(ref)) if any(c in ref for c in "*?[") else [self.root / ref]
            if any(p.exists() for p in matches):
                existing.append(ref)
                continue
            ref_lines = [i for i, line in enumerate(lines) if ref in line]
            context = " ".join(
                lines[max(0, i - 2) : min(len(lines), i + 3)] for i in ref_lines
            ) if False else ""
            # Simpler line-local new-file declaration check.
            is_new = any(
                re.search(r"\b(?:new file|create|add new)\b", lines[i], re.I)
                for i in ref_lines
            )
            if is_new:
                declared_new.append(ref)
            else:
                missing.append(ref)

        if missing:
            self.error(check, f"Pending inventory names missing files without declaring them new: {missing}", pending)

        required_fields = [
            "Requested outcome",
            "Affected files",
            "Exact edits by file",
            "Cross-reference and validation work",
            "Canon decisions required",
            "Status",
        ]
        for heading, body, line in split_h3_sections(text):
            for field in required_fields:
                if field.casefold() not in body.casefold():
                    self.error(check, f"Proposal '{heading}' is missing required field '{field}'.", pending, line)

        if not any(f.severity == "ERROR" and f.check == check for f in self.findings):
            self.pass_(
                check,
                f"Pending inventory verified: {len(headings)} proposal(s), {len(existing)} existing target(s), "
                f"{len(declared_new)} declared new file(s).",
            )



    # ------------------------------------------------------------------
    # Creature catalog integrity
    # ------------------------------------------------------------------
    def check_creature_catalog(self) -> None:
        check = "creature catalog integrity"
        required = [
            CREATURE_MANIFEST, CREATURE_DATA_JSON, CREATURE_DATA_CSV, CREATURE_INDEX
        ]
        missing = [path.as_posix() for path in required if not (self.root / path).is_file()]
        if missing:
            self.error(check, f"Required creature files are missing: {missing}.")
            return

        try:
            records = json.loads((self.root / CREATURE_DATA_JSON).read_text(encoding="utf-8"))
            manifest = json.loads((self.root / CREATURE_MANIFEST).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.error(check, f"Creature JSON could not be read: {exc}.")
            return

        if not isinstance(records, list):
            self.error(check, "Creature JSON must be a list.", self.root / CREATURE_DATA_JSON)
            records = []

        if len(records) != EXPECTED_CREATURE_COUNT:
            self.error(
                check,
                f"Expected {EXPECTED_CREATURE_COUNT} creature records; found {len(records)}.",
                self.root / CREATURE_DATA_JSON,
            )

        required_fields = {
            "name", "category", "catalog_group", "catalog_file", "entry_anchor",
            "availability", "stat_baseline", "cr", "size", "creature_type",
            "ac", "hp", "speed", "habitat", "elyndrian_regions",
            "campaign_status", "magical_dependency", "dead_zone_behavior",
            "recommended_party_levels", "suitable_gate_city",
            "physical_viability", "connection_severance", "dm_adjudication",
        }
        names: list[str] = []
        groups: set[str] = set()
        catalog_files: set[str] = set()
        index_text = (self.root / CREATURE_INDEX).read_text(encoding="utf-8")
        for record in records:
            if not isinstance(record, dict):
                self.error(check, "Every creature record must be an object.", self.root / CREATURE_DATA_JSON)
                continue
            name = str(record.get("name", "")).strip()
            names.append(normalize_name(name))
            groups.add(str(record.get("catalog_group", "")).strip())
            catalog_file = str(record.get("catalog_file", "")).strip()
            catalog_files.add(catalog_file)
            absent = sorted(field for field in required_fields if str(record.get(field, "")).strip() == "")
            if absent:
                self.error(check, f"Creature '{name or '<unnamed>'}' is missing fields: {absent}.", self.root / CREATURE_DATA_JSON)
                continue
            category_path = self.root / CREATURE_ROOT / catalog_file
            if not category_path.is_file():
                self.error(check, f"Creature '{name}' category file is missing: {catalog_file}.", self.root / CREATURE_DATA_JSON)
                continue
            category_text = self.text(category_path)
            heading_pattern = rf"^##\s+{re.escape(name)}\s*$"
            if not re.search(heading_pattern, category_text, re.M):
                self.error(check, f"Creature '{name}' has no matching H2 entry in {catalog_file}.", category_path)
            anchor = str(record.get("entry_anchor", "")).strip().casefold()
            if anchor not in markdown_anchors(category_text):
                self.error(check, f"Creature '{name}' anchor '#{anchor}' is missing in {catalog_file}.", category_path)
            expected_link = f"({catalog_file}#{anchor})"
            if expected_link not in index_text:
                self.error(check, f"Creature '{name}' is not directly linked from the catalog index.", self.root / CREATURE_INDEX)

        duplicate_names = sorted(name for name, count in Counter(names).items() if name and count > 1)
        if duplicate_names or any(not name for name in names):
            self.error(check, f"Creature names must be nonempty and unique; duplicates: {duplicate_names}.", self.root / CREATURE_DATA_JSON)
        if len(groups - {""}) != EXPECTED_CREATURE_GROUP_COUNT:
            self.error(check, f"Expected {EXPECTED_CREATURE_GROUP_COUNT} creature groups; found {sorted(groups - {''})}.", self.root / CREATURE_DATA_JSON)

        category_paths = sorted((self.root / CREATURE_ROOT / "catalog").rglob("*.md"))
        if len(category_paths) != EXPECTED_CREATURE_CATEGORY_COUNT:
            self.error(check, f"Expected {EXPECTED_CREATURE_CATEGORY_COUNT} category files; found {len(category_paths)}.", self.root / CREATURE_ROOT / "catalog")
        actual_catalog_files = {
            path.relative_to(self.root / CREATURE_ROOT).as_posix() for path in category_paths
        }
        if catalog_files != actual_catalog_files:
            self.error(
                check,
                f"Creature JSON category-file set differs from repository files: missing={sorted(actual_catalog_files - catalog_files)}, extra={sorted(catalog_files - actual_catalog_files)}.",
                self.root / CREATURE_DATA_JSON,
            )

        try:
            with (self.root / CREATURE_DATA_CSV).open(newline="", encoding="utf-8-sig") as handle:
                csv_rows = list(csv.DictReader(handle))
        except OSError as exc:
            self.error(check, f"Creature CSV could not be read: {exc}.", self.root / CREATURE_DATA_CSV)
            csv_rows = []
        csv_names = [normalize_name(row.get("name", "")) for row in csv_rows]
        if len(csv_rows) != EXPECTED_CREATURE_COUNT or Counter(csv_names) != Counter(names):
            self.error(check, "Creature CSV does not match the JSON creature-name inventory.", self.root / CREATURE_DATA_CSV)

        counts = manifest.get("counts", {}) if isinstance(manifest, dict) else {}
        expected_manifest_counts = {
            "creatures": EXPECTED_CREATURE_COUNT,
            "categories": EXPECTED_CREATURE_CATEGORY_COUNT,
            "repository_groups": EXPECTED_CREATURE_GROUP_COUNT,
            "markdown_category_entries": EXPECTED_CREATURE_COUNT,
            "roll_tables": EXPECTED_ROLL_TABLE_COUNT,
            "roll_results": EXPECTED_ROLL_RESULT_COUNT,
        }
        for key, expected in expected_manifest_counts.items():
            if counts.get(key) != expected:
                self.error(check, f"Creature manifest count '{key}' must be {expected}; found {counts.get(key)!r}.", self.root / CREATURE_MANIFEST)

        self._check_checksum_manifest(check, self.root / CREATURE_ROOT, manifest, self.root / CREATURE_MANIFEST)

        if not any(f.severity == "ERROR" and f.check == check for f in self.findings):
            self.pass_(
                check,
                f"Verified {EXPECTED_CREATURE_COUNT} creatures, {EXPECTED_CREATURE_CATEGORY_COUNT} category files, {EXPECTED_CREATURE_GROUP_COUNT} groups, direct index links, synchronized JSON/CSV, and manifest checksums.",
            )

    # ------------------------------------------------------------------
    # Random encounter roll-table integrity
    # ------------------------------------------------------------------
    def check_roll_tables(self) -> None:
        check = "random encounter roll-table integrity"
        required = [ROLL_MANIFEST, ROLL_DATA_JSON, ROLL_DATA_CSV, ROLL_ROOT / "Roll_Table_Index.md"]
        missing = [path.as_posix() for path in required if not (self.root / path).is_file()]
        if missing:
            self.error(check, f"Required roll-table files are missing: {missing}.")
            return
        try:
            results = json.loads((self.root / ROLL_DATA_JSON).read_text(encoding="utf-8"))
            manifest = json.loads((self.root / ROLL_MANIFEST).read_text(encoding="utf-8"))
            creatures = json.loads((self.root / CREATURE_DATA_JSON).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.error(check, f"Roll-table data could not be read: {exc}.")
            return

        if not isinstance(results, list):
            self.error(check, "Roll-table JSON must be a list.", self.root / ROLL_DATA_JSON)
            results = []
        if len(results) != EXPECTED_ROLL_RESULT_COUNT:
            self.error(check, f"Expected {EXPECTED_ROLL_RESULT_COUNT} roll results; found {len(results)}.", self.root / ROLL_DATA_JSON)

        creature_names = {normalize_name(str(record.get("name", ""))) for record in creatures if isinstance(record, dict)}
        table_rolls: dict[int, list[int]] = defaultdict(list)
        gate_results = 0
        result_keys: list[tuple[int, int]] = []
        for result in results:
            if not isinstance(result, dict):
                self.error(check, "Every roll result must be an object.", self.root / ROLL_DATA_JSON)
                continue
            table_number = int(result.get("table_number", 0) or 0)
            roll = int(result.get("roll", 0) or 0)
            table_rolls[table_number].append(roll)
            result_keys.append((table_number, roll))
            table_rel = str(result.get("table_file", "")).strip()
            table_path = self.root / ROLL_ROOT / table_rel
            if not table_path.is_file():
                self.error(check, f"Roll table file is missing: {table_rel}.", self.root / ROLL_DATA_JSON)
                continue
            table_text = self.text(table_path)
            for entry in result.get("catalog_entries", []):
                name = normalize_name(str(entry.get("name", "")))
                if name not in creature_names:
                    self.error(check, f"Roll result references unknown creature: {entry.get('name')!r}.", self.root / ROLL_DATA_JSON)
                anchor = str(entry.get("entry_anchor", "")).strip()
                catalog_file = str(entry.get("catalog_file", "")).strip()
                if f"#{anchor})" not in table_text or Path(catalog_file).name not in table_text:
                    self.error(check, f"Table {table_number} roll {roll} lacks a direct catalog link for {entry.get('name')!r}.", table_path)
            if result.get("gate_invasion") is True:
                gate_results += 1
                if int(result.get("total_creatures", 0) or 0) < 50:
                    self.error(check, f"Gate-invasion table {table_number} roll {roll} contains fewer than 50 creatures.", self.root / ROLL_DATA_JSON)

        duplicates = sorted(key for key, count in Counter(result_keys).items() if count > 1)
        if duplicates:
            self.error(check, f"Duplicate table/roll pairs exist: {duplicates}.", self.root / ROLL_DATA_JSON)
        if len(table_rolls) != EXPECTED_ROLL_TABLE_COUNT:
            self.error(check, f"Expected {EXPECTED_ROLL_TABLE_COUNT} roll tables; found {len(table_rolls)}.", self.root / ROLL_DATA_JSON)
        for table_number, rolls in table_rolls.items():
            if sorted(rolls) != [1, 2, 3, 4, 5, 6]:
                self.error(check, f"Table {table_number} must contain rolls 1-6 exactly once; found {sorted(rolls)}.", self.root / ROLL_DATA_JSON)
        if gate_results != EXPECTED_GATE_INVASION_RESULT_COUNT:
            self.error(check, f"Expected {EXPECTED_GATE_INVASION_RESULT_COUNT} gate-invasion results; found {gate_results}.", self.root / ROLL_DATA_JSON)

        table_paths = []
        for group in ("natural_ecology", "planar_and_magical", "constructs_and_animated", "gate_incursions"):
            table_paths.extend((self.root / ROLL_ROOT / group).glob("*.md"))
        if len(table_paths) != EXPECTED_ROLL_TABLE_COUNT:
            self.error(check, f"Expected {EXPECTED_ROLL_TABLE_COUNT} Markdown roll tables; found {len(table_paths)}.", self.root / ROLL_ROOT)

        try:
            with (self.root / ROLL_DATA_CSV).open(newline="", encoding="utf-8-sig") as handle:
                csv_rows = list(csv.DictReader(handle))
        except OSError as exc:
            self.error(check, f"Roll-table CSV could not be read: {exc}.", self.root / ROLL_DATA_CSV)
            csv_rows = []
        csv_keys = Counter((int(row.get("table_number", 0) or 0), int(row.get("roll", 0) or 0)) for row in csv_rows)
        if len(csv_rows) != EXPECTED_ROLL_RESULT_COUNT or csv_keys != Counter(result_keys):
            self.error(check, "Roll-table CSV does not match the JSON table/roll inventory.", self.root / ROLL_DATA_CSV)

        counts = manifest.get("counts", {}) if isinstance(manifest, dict) else {}
        expected_counts = {
            "tables": EXPECTED_ROLL_TABLE_COUNT,
            "results": EXPECTED_ROLL_RESULT_COUNT,
            "repository_groups": EXPECTED_CREATURE_GROUP_COUNT,
            "gate_invasion_results": EXPECTED_GATE_INVASION_RESULT_COUNT,
        }
        for key, expected in expected_counts.items():
            if counts.get(key) != expected:
                self.error(check, f"Roll manifest count '{key}' must be {expected}; found {counts.get(key)!r}.", self.root / ROLL_MANIFEST)
        if manifest.get("gate_invasion_minimum") != 50:
            self.error(check, "Roll manifest gate_invasion_minimum must be 50.", self.root / ROLL_MANIFEST)

        self._check_checksum_manifest(check, self.root / ROLL_ROOT, manifest, self.root / ROLL_MANIFEST)

        if not any(f.severity == "ERROR" and f.check == check for f in self.findings):
            self.pass_(
                check,
                f"Verified {EXPECTED_ROLL_TABLE_COUNT} d6 tables, {EXPECTED_ROLL_RESULT_COUNT} synchronized results, catalog links, {EXPECTED_GATE_INVASION_RESULT_COUNT} gate-invasion results, and manifest checksums.",
            )

    def _check_checksum_manifest(
        self, check: str, base: Path, manifest: object, manifest_path: Path
    ) -> None:
        files = manifest.get("files", []) if isinstance(manifest, dict) else []
        if not isinstance(files, list):
            self.error(check, "Manifest files field must be a list.", manifest_path)
            return
        for entry in files:
            if not isinstance(entry, dict):
                self.error(check, "Manifest file entry must be an object.", manifest_path)
                continue
            rel = str(entry.get("path", "")).strip()
            target = base / rel
            if not target.is_file():
                self.error(check, f"Manifest file does not exist: {rel}.", manifest_path)
                continue
            raw = target.read_bytes()
            actual_sha = hashlib.sha256(raw).hexdigest()
            if actual_sha != str(entry.get("sha256", "")):
                self.error(check, f"Manifest checksum mismatch: {rel}.", target)
            if len(raw) != entry.get("bytes"):
                self.error(check, f"Manifest byte count mismatch: {rel}.", target)


# ----------------------------------------------------------------------
# Parsing helpers
# ----------------------------------------------------------------------

def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def normalize_name(value: str) -> str:
    value = value.replace("“", '"').replace("”", '"').replace("’", "'")
    value = re.sub(r"[*_`]+", "", value)
    value = re.sub(r"\s+", " ", value).strip().casefold()
    return value


def normalize_heading(value: str) -> str:
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"\s+", " ", value).strip().casefold()
    return value


def canonical_npc_name(value: str) -> str:
    value = value.split(" — ", 1)[0].split(" - ", 1)[0].strip()
    value = TITLE_PREFIXES.sub("", value)
    return normalize_name(value)


def section_between(text: str, start_pattern: str, end_pattern: str) -> str:
    start = re.search(start_pattern, text, re.M)
    if not start:
        return ""
    end = re.search(end_pattern, text[start.end() :], re.M)
    if not end:
        return text[start.end() :]
    return text[start.end() : start.end() + end.start()]


def extract_city_bullets(section: str) -> list[str]:
    cities: list[str] = []
    for raw in re.findall(r"^-\s+(.+?)\s*$", section, re.M):
        value = re.sub(r"\s*\([^)]*\)\s*$", "", raw).strip()
        if re.match(r"^\d+\s+", value):
            continue
        if value.casefold() in {"6 elven", "6 dwarven", "8 elven", "8 dwarven", "4 mixed"}:
            continue
        cities.append(value)
    return cities


def split_h2_sections(text: str) -> list[tuple[str, str, int]]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.M))
    result: list[tuple[str, str, int]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result.append((match.group(1).strip(), text[match.end() : end], line_number(text, match.start())))
    return result


def split_h3_sections(text: str) -> list[tuple[str, str, int]]:
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", text, re.M))
    result: list[tuple[str, str, int]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result.append((match.group(1).strip(), text[match.end() : end], line_number(text, match.start())))
    return result


def markdown_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    counts: Counter[str] = Counter()
    for _, heading in HEADING_RE.findall(text):
        slug = heading.strip().casefold()
        slug = re.sub(r"[`*_]", "", slug)
        slug = re.sub(r"[^\w\- ]", "", slug)
        slug = re.sub(r"\s+", "-", slug)
        base = slug
        suffix = counts[base]
        counts[base] += 1
        anchors.add(base if suffix == 0 else f"{base}-{suffix}")
    return anchors


def strip_code(text: str) -> str:
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def active_pending_text(text: str) -> str:
    start = re.search(r"^## Active Proposed Changes\s*$", text, re.M)
    end = re.search(r"^## Required Proposal Format\s*$", text, re.M)
    if not start:
        return ""
    if end and end.start() > start.end():
        return text[start.end() : end.start()]
    return text[start.end() :]


def parse_index_file_rows(text: str) -> dict[str, dict[str, str | int]]:
    rows: dict[str, dict[str, str | int]] = {}
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.startswith("|") or "File" not in line:
            index += 1
            continue
        headers = [cell.strip().casefold() for cell in line.strip("|").split("|")]
        if "file" not in headers:
            index += 1
            continue
        if index + 1 >= len(lines) or not re.match(r"^\|(?:\s*:?-+:?\s*\|)+$", lines[index + 1]):
            index += 1
            continue
        index += 2
        while index < len(lines) and lines[index].startswith("|"):
            cells = [cell.strip() for cell in lines[index].strip("|").split("|")]
            if len(cells) == len(headers):
                row: dict[str, str | int] = dict(zip(headers, cells))
                file_cell = row.get("file", "")
                match = re.search(r"`([^`]+\.(?:md|py|ya?ml|json))`", str(file_cell), re.I)
                if match:
                    row["line"] = index + 1
                    rows[match.group(1)] = row
            index += 1
    return rows


def extract_location_owner_entries(section: str) -> list[tuple[str, str | None]]:
    result: list[tuple[str, str | None]] = []
    for match in re.finditer(r"^-\s+\*\*(.+?)\*\*", section, re.M):
        bold = match.group(1).strip()
        if " — " in bold:
            location, owner_part = bold.split(" — ", 1)
            owner = owner_part.split(":", 1)[0].strip()
            result.append((location.strip(), owner))
        else:
            location = bold.rstrip(":").strip()
            result.append((location, None))
    return result


def render_text(findings: Iterable[Finding]) -> str:
    findings = list(findings)
    lines: list[str] = []
    for finding in findings:
        location = ""
        if finding.file:
            location = f" {finding.file}"
            if finding.line:
                location += f":{finding.line}"
        lines.append(f"[{finding.severity}] {finding.check}:{location} {finding.message}")
    counts = Counter(f.severity for f in findings)
    lines.append("")
    lines.append(
        "Summary: "
        f"{counts.get('ERROR', 0)} error(s), "
        f"{counts.get('WARN', 0)} warning(s), "
        f"{counts.get('PASS', 0)} passed check(s)."
    )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root (default: current directory)")
    parser.add_argument("--json", type=Path, help="Optional path for a JSON findings report")
    parser.add_argument("--strict-warnings", action="store_true", help="Return exit code 2 when warnings exist without errors")
    args = parser.parse_args(argv)

    validator = Validator(args.root)
    validator.run()
    print(render_text(validator.findings))

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps([asdict(finding) for finding in validator.findings], indent=2),
            encoding="utf-8",
        )

    errors = sum(f.severity == "ERROR" for f in validator.findings)
    warnings = sum(f.severity == "WARN" for f in validator.findings)
    if errors:
        return 1
    if warnings and args.strict_warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
