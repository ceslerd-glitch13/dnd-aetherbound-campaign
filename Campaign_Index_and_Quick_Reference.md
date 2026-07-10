# Campaign Index and Quick Reference

**Campaign Title:** Untitled D&D Campaign (Homebrew – Magic Dead Zones, Dimensional Gates, Aetheron Plot)  
**Current Version / Focus:** v2.10 (July 2026) – Early campaign refinement complete. Primary play focus: Sessions 0–5 in/around Ravensport with branching paths (medallion, smuggling ring, Deepanvil delivery/mines). High-level arc available as stretch goal.  
**Last Major Update:** Implementation of all recommended cleanups, organization improvements, NPC deepening, encounter quick reference, and early sessions plan. All changes follow existing Guidelines (especially World Update Change Management, Battle Stat Block Management, NPC Creation). No core mechanics altered.  
**Continent Name:** Elyndria (set for consistency; previously "To be named").

**Purpose of This Index:** Single source of truth for file organization, purposes, interconnections, and quick navigation. Addresses previous recommendation for better labeling/organization in a flat directory structure. Update this file whenever new documents or major changes are added.

---

## File Organization & Directory

All files are in `/home/workdir/attachments/`. Use this index to locate content quickly. For long-term scalability, consider the recommended folder hierarchy in the Early Sessions Plan or future migration (e.g., 00_Overview/, 01_Locations/, 02_NPCs/, etc.), but current flat structure is functional with this index.

### Core Lore & World Documents (Start Here for Big Picture)
- **DnD_Campaign_World_Bible.md** (v2.10 – cleaned)  
  **Purpose**: Central high-level lore bible (races, dead zones/Aetheron origin, gates, cities overview, pantheon, rules/homebrew, key locations like Ravensport).  
  **Status**: Duplicate "Related Documents" section removed. Added reference to early sessions focus and Early_Sessions_Plan. Minor version bump.  
  **Interconnections**: Primary index; cross-references all city profiles, guidelines, and core files. Update first for major lore changes.

- **World_Geography.md** (enhanced)  
  **Purpose**: Continent layout, regions, dead zones placement, starter area details.  
  **Status**: Added specific travel times and descriptions for Ravensport starter area (western road, nearby dead zone ~2 hours walking). Continent name set to Elyndria. Hidden Deepanvil plot note preserved.  
  **Interconnections**: Supports map creation guideline and Early Sessions Plan (travel to Deepanvil path).

- **Early_Sessions_Plan_Sessions_0_to_5.md** (NEW – primary for initial play)  
  **Purpose**: Focused plan for Session 0 + branching paths for Sessions 1–5. Includes detailed outlines, 4 interconnected quest paths (medallion keep/return, Deepanvil delivery + mine subquests, Shrouded Wards smuggling), pre-created key NPCs with full details (appearance, personality, motivation, secret, quirk), encounter templates (D&D Beyond pointers + partial homebrew), textual map/location aids, and convergence to main plot.  
  **Status**: Created to implement review recommendations for early campaign focus, branching agency, and pre-created NPCs.  
  **Interconnections**: References and updates starter quest, NPC file, stat blocks, city profiles, and World Bible. Use this first for Sessions 0–5 prep.

### City & Location Profiles (Detailed Playable Locations)
- **Ravensport_City_Profile.md**  
  **Purpose**: Full details for primary hub (leadership, shops with named proprietors, districts, economy, defenses, plot hooks).  
  **Status**: Current; cross-referenced in early plan. Some NPC overlap with master file (disambiguation notes added in NPC file).  
  **Interconnections**: Core for Session 0 (The Rusty Anchor, Docks, Shrouded Wards, Grand Bazaar).

- **Deepanvil_City_Profile.md**, **Faerindel_City_Profile.md**, **Ironforge_City_Profile.md**  
  **Purpose**: Supporting gate/mining cities for later expansion or specific paths (e.g., Deepanvil for western delivery quest).  
  **Status**: Complete per City Creation Guidelines. Use when players travel (e.g., Path 3 in early plan).  
  **Interconnections**: Linked from World Bible, Geography, and Early Sessions Plan (Deepanvil subquests).

- **Ravensport_Starter_Area_Key_Locations.md** (RECOMMENDED / to be expanded)  
  **Purpose**: Textual quick-reference "map" aid for Sessions 0–5 (districts, travel times within city, key sites like Rusty Anchor / Last Chance Curios / western road / nearby dead zone, sensory descriptions, rumors tying to branching paths). Addresses map creation weakness with narrative focus.  
  **Status**: Prioritized in review; create or expand from existing district info in Ravensport profile if not yet present.  
  **Interconnections**: Companion to Early Sessions Plan and Ravensport profile.

### NPC & Character Management
- **NPC_Backstory_Personality_file.md** (updated)  
  **Purpose**: Master living database – all named NPCs sorted by city/role. Includes major/minor for consistency.  
  **Status**: Key early campaign NPCs deepened with full details from Early Sessions Plan (Rurik expanded, Lirael "Silverthorn" deepened, new Client/Agent, new Smuggling Ring Leader, Deepanvil liaison, etc.). Disambiguation notes added for repeated names across cities (Lirael, Vesper, Helga, Thrain, Garrick, Brannok, Drogath, Vorn – distinguish by full title + location/role). New "Quest-Relevant / Early Campaign NPCs" subsection under Ravensport.  
  **Interconnections**: Update whenever new NPCs added (per its own purpose note). Cross-reference in city profiles and Early Sessions Plan. Use 3-line + deeper method per NPC Creation Guideline.

### Quests, Sessions & Plot
- **Captain_Ruriks_Request_Session_0-1 (1).md** (updated)  
  **Purpose**: Starter quest hook at The Rusty Anchor (medallion theft).  
  **Status**: Investigation leads section expanded with concrete branching options tied to the four paths. References Early_Sessions_Plan for full structure.  
  **Interconnections**: Core of Session 0; links to all branching paths and Early Sessions Plan.

- **Early_Sessions_Plan_Sessions_0_to_5.md** (see above)  
  Primary for all early quest branching and session prep.

### Encounters, Stat Blocks & Combat
- **Enemy_Encounters_Stat_Blocks.md** (updated)  
  **Purpose**: Master repository for all custom stat blocks (guards, monsters, NPCs). Standard format with AC/HP/attacks/loot/notes.  
  **Status**: Added "Quick Reference: Common Encounters for Sessions 0–5" section with D&D Beyond pointers for official blocks + partial homebrew skeletons/adjustments for dead zones, Aetherbound, smuggling, mining threats. Follows Battle Stat Block Management Guideline strictly (check here first).  
  **Interconnections**: Update with any new threats from play. Used in Early Sessions Plan encounters.

### Guidelines (Process Documents – Do Not Deviate)
- **Guideline_Battle_Stat_Block_Management.md**  
- **City_Creation_Guidelines.md**  
- **Guideline_World_Update_Change_Management.md** (core rule: implement requested changes, then update affected files)  
- **Guideline_Quest_Creation.md**  
- **Guideline_NPC_Character_Creation.md** (3-line method + deeper for key NPCs)  
- **Guideline_World_Geography_Map_Creation.md**  
- **Guideline_World_Update_Change_Management.md** (already followed in all cleanups)

**Usage Note**: Always consult the relevant Guideline before creating/editing content. The Early Sessions Plan incorporates all of them for the starter arc.

### Other / Future Expansion
- **Captain_Ruriks_Request_Session_0-1 (1).md** and Early plan cover initial quests. Additional quests can be added to Early_Sessions_Plan or a new master quest tracker as needed.
- Pantheon (in World Bible): Foundational (Aetherion, Elyndra, Thalor). Room for 1–2 more (e.g., dwarven forge god, general trade/war deity) per review recommendation – implement when relevant to play.
- Dragons, full 10 dead zones details, factions, random tables: Noted in World Bible/ Geography as future expansion. Prioritize only when players approach those elements.
- Player character creation notes or restrictions: Can be added to Early Sessions Plan or new file if needed for Session 0.

---

## Quick Navigation for Common Tasks

- **Running Session 0 or prepping Sessions 1–5**: Start with **Early_Sessions_Plan_Sessions_0_to_5.md** + updated starter quest + Ravensport profile + deepened NPCs in master file + Quick Reference in stat blocks.
- **Adding a new NPC**: Use NPC Creation Guideline → add to master NPC file (with disambiguation if name overlap) → update relevant city profile if shop/leadership → note in this Index.
- **New stat block or encounter**: Check stat blocks file first → add in standard format or to Quick Reference section → update Early Sessions Plan if for early game.
- **World/lore change**: Follow World Update Change Management Guideline → update World Bible + affected profiles/geography/NPC file → update this Index and Early Sessions Plan if relevant to starter arc.
- **Map or geography**: Use Geography file + map creation guideline. For starter area, use textual aids in Early Sessions Plan or dedicated Ravensport_Starter_Area_Key_Locations.md.
- **City expansion**: Follow City Creation Guidelines strictly → create new profile if large settlement.

---

## Notes on Cleanup & Refinements Implemented

- All recommendations from full project review addressed: redundancies removed (World Bible duplicate), organization improved (this Index + Early Sessions Plan as hub), NPCs pre-created and disambiguated, encounters enhanced with D&D Beyond + partial fills, early campaign focused with branching paths exactly as specified, textual map aids prioritized, pantheon noted for future, geography starter details added.
- Embedded notes in files reviewed and actioned (e.g., "update this file whenever new locations or personnel added" → done via Index and master NPC updates; "See previous version" in starter quest → replaced with concrete leads; "Ready for further refinement" → implemented early focus and cleanups).
- No core mechanics changed. All homebrew (dead zones, Aetherite) preserved.
- Versioning applied (World Bible to v2.10). This Index serves as living changelog hub.
- Continent name set to **Elyndria** for consistency in Geography and references.

**End of Campaign Index**  
Update this file with every significant addition or cleanup. It ensures the project remains efficient, consistent, and easy to navigate long-term. Ready for play or further expansion.