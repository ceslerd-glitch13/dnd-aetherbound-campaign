# Creature Data Schema

> **Repository role:** Field guide for `creatures.json` and `creatures.csv`. The JSON file is the structured catalog record; CSV is a tabular mirror.

## Structural fields

| Field | Meaning |
|---|---|
| `name` | Unique creature name used for lookup. |
| `category` | Original catalog category. |
| `catalog_group` | Repository group: `natural_ecology`, `planar_and_magical`, `constructs_and_animated`, or `gate_incursions`. |
| `catalog_file` | Repository-relative category Markdown path beneath `creatures/`. |
| `entry_anchor` | Markdown anchor for the creature entry. |

## Rules and source fields

| Field | Meaning |
|---|---|
| `availability` | Edition/source availability note supplied by the catalog. |
| `stat_baseline` | Official source used as the planning baseline. |
| `cr`, `size`, `creature_type` | Basic encounter-identification fields. |
| `ac`, `hp`, `speed`, `str`, `dex`, `con`, `int`, `wis`, `cha` | Quick comparison values, not a complete stat block. |
| `senses`, damage fields, and condition fields | Defensive and sensory reference. |

## Campaign-placement fields

| Field | Meaning |
|---|---|
| `habitat` | General habitat from the selected source or planning pass. |
| `elyndrian_regions` | Proposed campaign placement or incident context. |
| `campaign_status` | Catalog classification or recommendation; not automatic setting canon. |
| `recommended_party_levels` | Planning range, not an encounter-balance guarantee. |
| `suitable_gate_city` | Gate-city or major-hub suitability. |

## Dead-zone and adjudication fields

| Field | Meaning |
|---|---|
| `physical_viability` | Whether the body can continue without active magic. |
| `magical_dependency` | Relative dependency on active magic. |
| `connection_severance` | External magical links expected to fail. |
| `dead_zone_behavior` | Creature-specific catalog recommendation, subordinate to the World Bible. |
| `dm_adjudication` | Decision that remains with the Dungeon Master. |

## Encounter-use fields

| Field | Meaning |
|---|---|
| `strengths_advantages` | Short tactical summary. |
| `weaknesses_disadvantages` | Short tactical weakness summary. |
| `verification` | Source-check status or reminder. |

## Maintenance rule

Update the JSON record first, regenerate the CSV and Markdown lookup views, update the manifest hashes, and run repository validation. Never hand-edit one generated view without synchronizing the others.
