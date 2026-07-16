---
status: Active Reference
authority: Proposed Change Staging
version: 2.6
last_reviewed: 2026-07-16
---

# Pending Changes — Active

## Purpose

This file contains proposed repository changes that have not yet been implemented. Individual decisions may be marked approved while the larger batch remains under discussion. It is not canon until the approved batch is applied to the authority files.

Read `GOVERNANCE.md` and `SKILL.md` before using this file.

## Active Proposed Changes

### Batch B-01 — Dead zones, divine power, and magical transport

- **Requested outcome:** Establish one consistent rule explaining how dead zones suppress magic, magical transport, divine perception, divine manifestations, and gods physically present inside a zone.
- **Affected files:**
  - `DnD_Campaign_World_Bible.md`
  - `Early_Sessions_Plan_Sessions_0_to_5.md`
  - `Enemy_Encounters_Stat_Blocks.md`
- **Exact edits by file:**
  - `DnD_Campaign_World_Bible.md`: Replace the contradictory statements about gods and dead zones with the following canon framework:
    - A dead zone prevents magical energy from entering, leaving, or remaining stable within its boundary.
    - Spellcasting and magical item effects fail inside the zone unless a separately approved exception applies.
    - Teleportation, portals, dimensional travel, magical communication, scrying, divination, divine observation, and similar effects fail when either endpoint or required path lies inside a dead zone because magic is required at both ends.
    - Existing or lingering magical effects end immediately or decay far faster than normal after entering the zone, according to the specific effect and DM judgment.
    - A deity outside the zone is not harmed at its source but cannot project power, perception, miracles, avatars, or magical influence through the boundary.
    - A deity, true manifestation, avatar, or other divine being physically present inside a dead zone experiences magical drain. The drain does not directly injure or kill the deity, but it suppresses external reinforcement and gradually exhausts accessible divine power.
    - In the theoretical case of extraordinarily prolonged isolation inside a dead zone, with no worship, divine energy, or magical reinforcement able to reach the deity, the deity could eventually lose its godhood. This is a description of the zone's maximum effect, not a current campaign event.
    - Magic items are normally suppressed rather than permanently destroyed, unless a specific item or event states otherwise.
  - `Early_Sessions_Plan_Sessions_0_to_5.md`: Align all dead-zone explanations with the World Bible rule above. Do not imply that magical transport, divine observation, or outside spell support can freely cross a dead-zone boundary. Preserve beacon-core details as unresolved until Batch B-02 is approved.
  - `Enemy_Encounters_Stat_Blocks.md`: Add encounter guidance stating that magical creatures, summoned beings, avatars, ongoing magical effects, magical movement, and magical escape abilities are suppressed or drained inside dead zones. Exact creature-specific consequences remain subject to the stat-block guideline and DM judgment.
- **Cross-reference and validation work:**
  - Search for statements that gods are unaffected by dead zones or can manifest freely inside them and replace them with the approved framework.
  - Search for teleportation, portal, scrying, communication, summoning, and divine-intervention references involving dead zones.
  - Do not resolve the Resonance Medallion or beacon-core exception in this change; those require separate decisions.
- **Canon decisions required:** None for this proposal. The dead-zone and godhood interpretation was approved during Batch B discussion.
- **Status:** Decision approved; awaiting completion and approval of the full Batch B implementation set.


### Batch B-02 — Beacon-core resonance field

- **Requested outcome:** Preserve the intended 20-foot supercharged-magic area around an active beacon core while defining exact casting cost, risk, duration, damage, and healing mechanics.
- **Affected files:**
  - `DnD_Campaign_World_Bible.md`
  - `Early_Sessions_Plan_Sessions_0_to_5.md`
  - `Enemy_Encounters_Stat_Blocks.md`
- **Exact edits by file:**
  - `DnD_Campaign_World_Bible.md`: Add the following beacon-core canon:
    - An active beacon core draws magical energy from the surrounding dead zone and transmits it to the Aetherian home world.
    - Within **20 feet** of the active core, the concentration of gathered magic creates a supercharged resonance field where ordinary spellcasting becomes possible despite the surrounding dead zone.
    - The field is not inherently destabilizing, but channeling its concentrated magic is difficult. Every spellcast requires a Constitution check using the spell's original level: **DC 10 + original spell level**; cantrips use **DC 10**.
    - On a failed check, the spell produces wild-magic behavior or another unintended outcome chosen by the DM according to the spell, caster, target, and situation.
    - On a successful check, the spell consumes a slot equal to half its original level, rounded up:
      - 2nd → 1st
      - 3rd → 2nd
      - 4th → 2nd
      - 5th → 3rd
      - 6th → 3rd
      - 7th → 4th
      - 8th → 4th
      - 9th → 5th
    - First-level spells are treated as cantrips for slot expenditure while cast inside the field and may be cast without consuming a spell slot.
    - The caster must still know or prepare the spell and must normally be capable of casting spells of that original level. The field reduces cost; it does not teach or unlock higher-level spells.
    - The spell retains its original spell level for Counterspell, Dispel Magic, concentration, scaling, and all other rules except slot expenditure.
    - A spell cast inside the field has **twice its normal duration** while its maintained effect remains within the 20-foot radius.
    - When the spell's subject, maintained area, or relevant magical effect leaves the field, divide its remaining enhanced duration by two. This restores the spell to the duration it would effectively have without continued resonance support.
    - A damaging spell deals an additional **1d6 force damage** to each creature it damages, once per creature per casting, not once per ray, missile, attack roll, or separate damage instance.
    - A healing spell restores an additional **1d6 hit points** to each creature it heals, once per creature per casting.
    - The flat 1d6 increase is intentional: it materially improves weaker spells while having proportionally less effect on stronger spells.
  - `Early_Sessions_Plan_Sessions_0_to_5.md`: Replace the abbreviated beacon-core note with the exact mechanics above and identify the rule as hidden, high-level campaign information unless discovered in play.
  - `Enemy_Encounters_Stat_Blocks.md`: Add a beacon-core environmental-effects reference for encounters occurring within 20 feet of an active core, including the Constitution check, reduced slot cost, doubled duration while maintained inside the field, duration reversion on exit, and flat damage/healing increase.
- **Cross-reference and validation work:**
  - Remove or revise any statement that the core grants automatic advantage on spells or a flat +2d10 bonus.
  - Preserve the normal dead-zone rules everywhere outside the 20-foot resonance field.
  - Ensure teleportation and other magical transport can operate only if the spell is cast and both required endpoints can sustain magic; leaving the core field into the surrounding dead zone can still cause the transport to fail.
  - Apply the extra 1d6 only once per affected creature per spellcasting to prevent multi-hit spells from multiplying the bonus.
- **Canon decisions required:** None for this proposal. Radius, casting check, reduced slot cost, duration rule, and damage/healing bonuses were approved during Batch B discussion.
- **Status:** Decision approved; awaiting completion and approval of the full Batch B implementation set.


### Batch B-03 — Resonance Medallion and Aetherian crystal-orb mechanics

- **Requested outcome:** Define the Resonance Medallion as a housing for an unmarked Aetherian crystal orb and establish exact rules for its protection field, stored energy, spellcasting use, recharge, exhaustion interaction, and technological classification.
- **Affected files:**
  - `Captain_Ruriks_Request_Session_0-1.md`
  - `DnD_Campaign_World_Bible.md`
  - `NPC_Backstory_Personality_file.md`
  - `Quests_Player_Decisions_Impacts.md`
- **Exact edits by file:**
  - `DnD_Campaign_World_Bible.md`: Expand Aetherian crystal technology into two related orb types:
    - **Inscribed orbs** contain internal runes and hold one predetermined spell of up to 3rd level. They can cast that stored spell when charged and can also serve as the active spell component in specialized Aetherian gun-like devices.
    - **Unmarked orbs** contain concentrated raw magical energy without a preset spell. They function as rechargeable batteries, resonance sources, and power intermediaries for Aetherian devices or creatures able to draw directly from them.
    - Specialized Aetherian gun-like devices combine one inscribed orb with one or more unmarked orbs. The inscribed orb defines the spell, while the unmarked orbs provide additional energy for repeated casting or upcasting.
    - A fully charged unmarked orb has **24 charges**.
    - A depleted orb fully recharges over **24 hours** while exposed to usable ambient magic, regaining **1 charge per hour**.
    - It cannot recharge inside a normal dead zone unless another approved source of usable magic is present.
    - One fully charged unmarked orb therefore equals either **24 hours of dead-zone field operation** or the energy cost of **one 3rd-level spell**, before accounting for mixed use.
    - **Veyne's Aetheron travel array** uses exactly **three Aetherite crystals**:
      - one rune-inscribed crystal containing the planar-transit formula and Aetheron destination key;
      - two fully charged unmarked crystal orbs acting as batteries.
    - The inscribed crystal's **standalone output** remains limited to 3rd-level power. Its more complex transit formula cannot activate without the additional unmarked batteries.
    - The completed three-crystal array has 72 charges available. A Plane Shift-equivalent effect requires 56 charges, so two crystals alone are insufficient and all three crystals must be connected for activation.
    - One successful trip consumes 56 charges from the combined array. The remaining 16 charges stay in the connected crystal pool unless another effect, failed activation, or campaign event consumes them.
    - The unmarked orb hidden in the Resonance Medallion was being delivered to Veyne as one of the battery components needed for this travel system.
  - `Captain_Ruriks_Request_Session_0-1.md`: Replace the vague Resonance Medallion description with these exact rules:
    - The silver medallion is only a concealed protective housing. The valuable component is the smooth, unmarked crystal orb inside it.
    - The orb requires **no attunement**.
    - While carried, worn, mounted, or placed, the orb creates a **5-foot-radius resonance field centered on itself**.
    - The field affects the holder and any creature directly adjacent to the orb.
    - The orb spends **1 charge per hour** while maintaining this field inside a dead zone. This is one charge for the field as a whole, not one charge per protected creature.
    - While charges remain, creatures inside the field are protected from the dead zone's direct magical drain and may cast spells by drawing power from the orb.
    - A spell cast through the orb consumes **8 charges per spell level**:
      - 1st level: 8 charges
      - 2nd level: 16 charges
      - 3rd level: 24 charges
    - The crystal system described here does not independently support spells above 3rd level. Effects beyond that limit require multiple power sources, larger infrastructure, or another separately approved mechanism.
    - **Cantrips consume no charges.** They cannot be upcast and do not draw from the orb's spell-level battery cost.
    - The caster must still know or prepare the spell and must normally be capable of casting it. The orb supplies magical energy; it does not teach spells or grant new spell levels.
    - Instantaneous spell effects may resolve normally when powered by the orb.
    - Ongoing, concentration, or persistent magical effects remain stable only while the relevant caster, target, or maintained effect remains within the orb's 5-foot field. Leaving the field inside a dead zone subjects the effect immediately to the normal dead-zone suppression rules.
    - Magical transport requires usable magic at every necessary endpoint. The orb can support the endpoint within its field, but teleportation, portals, or planar travel still fail if another required endpoint lies in an unprotected dead zone.
    - While protected by a charged orb, creatures do not accumulate Magical Exhaustion from the dead zone. If the orb reaches 0 charges, normal dead-zone effects begin immediately; protected time does not retroactively create exhaustion.
    - The orb may be removed from the medallion and used as a portable battery, stationary resonance source, component in machinery, or power source for an Aetherian weapon.
  - `NPC_Backstory_Personality_file.md`: Update any NPC knowledge, motives, secrets, or dialogue concerning the stolen medallion so informed NPCs understand that the medallion is merely a housing and that the unmarked orb is the valuable Aetherian technology.
  - `Quests_Player_Decisions_Impacts.md`: Track possession, current charge total, recharge time, use inside dead zones, spell-energy expenditure, and any transfer of the orb between the medallion, a character, or another device.
- **Cross-reference and validation work:**
  - Replace references that treat the necklace itself as the source of power.
  - Align the existing Aetherite crystal and Aetherian weapon descriptions with the inscribed-orb/unmarked-orb distinction.
  - Ensure charge use is cumulative: hourly field maintenance and spellcasting both draw from the same 24-charge pool.
  - Ensure the field is centered on the physical orb, not permanently tied to a wearer.
  - Preserve the distinction between the portable 5-foot resonance field and the beacon core's 20-foot supercharged field.
  - Align Veyne's travel references with the three-crystal array: one inscribed transit crystal plus two unmarked battery orbs.
  - Do not introduce a separate transit artifact when the established Aetherite crystal system can perform the function.
- **Canon decisions required:** None for this proposal. Classification, range, lack of attunement, 24-charge capacity, 24-hour recharge, protection cost, 3rd-level maximum, spell costs, and free cantrips were approved during Batch B discussion.
- **Status:** Decision approved; awaiting completion and approval of the full Batch B implementation set.


### Batch B-04 — Ravensport government and military command

- **Requested outcome:** Replace the conflicting Ravensport councils and military chains with one government that preserves the city's intended mixed civic, commercial, magical, and gate-security leadership.
- **Affected files:**
  - `DnD_Campaign_World_Bible.md`
  - `Ravensport_City_Profile.md`
  - `NPC_Backstory_Personality_file.md`
  - `Enemy_Encounters_Stat_Blocks.md`
  - `Captain_Ruriks_Request_Session_0-1.md`
  - `Early_Sessions_Plan_Sessions_0_to_5.md`
  - any other starter or session material that names Ravensport officials
- **Exact edits by file:**
  - `DnD_Campaign_World_Bible.md`: Replace all conflicting Ravensport government and military lists with this canonical structure:
    - **Lord Protector Elara Voss** is Ravensport's current civilian ruler and chairs the City Council. She controls civil administration, diplomacy, taxation, appointments, and emergency civilian authority.
    - **Harlan Voss** is the retired former Lord Protector and Elara's father. He may advise privately but holds no operational command or governing vote unless Elara formally delegates a temporary duty.
    - **Gate Warden Seraphine Vale** is a voting council member responsible for gate-security policy, defensive readiness, Iron Talon doctrine, and coordination between military branches.
    - **Master of Trade Vorn Ironvein** is a voting council member representing merchant guilds, dimensional commerce, tariffs, logistics, and major trade interests.
    - **Archmage Lirael Starveil** is a voting council member responsible for the Arcane Wardens, magical threats, dimensional research, and technical advice concerning the gate.
    - **Captain of the City Guard Thorne Blackwood** is a voting council member responsible for ordinary law enforcement, district patrols, investigations, and civil order outside the gate fortress.
    - **Gate Commander Kael Thorne** is the operational commander of the gate fortress and the Iron Talons. He reports to Gate Warden Seraphine Vale, executes approved security policy, and has tactical authority during an active gate emergency.
    - Kael Thorne is not a permanent voting member of the City Council, but attends security sessions and may exercise emergency tactical command within the gate complex.
    - Kael Thorne and Thorne Blackwood are unrelated; the similarity between Kael's surname and Blackwood's given name is coincidental.
    - Remove or replace the conflicting active offices and command roles assigned to Lord Harlan Voss, Lady Elara Voss as Spymaster, Captain-General Marcus Hale, Commander Kael "Ironwall" Thorne as an independent supreme commander, and any duplicate council lists.
    - Standardize the **Iron Talons at 200 active members total**, organized as four companies of 50 under Kael's operational command and Seraphine's strategic oversight.
    - Preserve approximately 1,800 total active military personnel: approximately 1,000 assigned to gate-fortress security and approximately 800 assigned to city-wide guard duties. Synchronize component totals so Iron Talons are not counted twice.
  - `Ravensport_City_Profile.md`: Replace the Leadership and Government summaries with the canonical structure above. Clearly distinguish the City Council, the city guard, the Arcane Wardens, and operational gate command.
  - `NPC_Backstory_Personality_file.md`: Consolidate each official into one identity and role. Reclassify Harlan Voss as retired. Add or revise concise profiles for Elara Voss, Seraphine Vale, Vorn Ironvein, Lirael Starveil, Thorne Blackwood, and Kael Thorne using their canonical responsibilities.
  - `Enemy_Encounters_Stat_Blocks.md`: Align guard categories and command notes with the new chain. Standard city guards answer to Thorne Blackwood; Arcane Wardens answer to Lirael Starveil; Iron Talons and gate-fortress forces answer operationally to Kael Thorne under Seraphine Vale's strategic authority.
  - starter/session material: Replace references to superseded offices or commanders. Use the specific official appropriate to the scene rather than referring vaguely to a conflicting "High Council."
- **Cross-reference and validation work:**
  - Search for Harlan Voss, Elara Voss, Seraphine Vale, Vorn Ironvein, Lirael Starveil, Thorne Blackwood, Kael Thorne, Marcus Hale, Iron Talons, Gate Wardens, City Council, and High Council.
  - Ensure the same person does not simultaneously hold conflicting civilian, intelligence, commercial, magical, and military positions.
  - Ensure the 200 Iron Talons are not also presented as 280 elsewhere.
  - Preserve Ravensport's intended government model: one civilian ruler supported by a mixed council, with separate civil and gate-security chains.
- **Canon decisions required:** None for this proposal. The user authorized corrective consolidation as long as the original intended functions are preserved.
- **Status:** Decision approved; awaiting completion and approval of the full Batch B implementation set.

### Batch B-05 — Captain Elandor "Blackscale" Rurik

- **Requested outcome:** Establish one Captain Rurik who retains the intended functions of Rusty Anchor proprietor, experienced sailor, and starter-quest giver.
- **Affected files:**
  - `Ravensport_City_Profile.md`
  - `NPC_Backstory_Personality_file.md`
  - `Captain_Ruriks_Request_Session_0-1.md`
  - `Quests_Player_Decisions_Impacts.md`
  - `Early_Sessions_Plan_Sessions_0_to_5.md`
  - any other file referring to Captain Rurik Voss or Captain Rurik
- **Exact edits by file:**
  - All affected files: Standardize the character as **Captain Elandor "Blackscale" Rurik**, human male.
  - `Ravensport_City_Profile.md`: Replace Captain Rurik Voss as proprietor of The Rusty Anchor with Elandor Rurik.
  - `NPC_Backstory_Personality_file.md`: Remove the duplicate Captain Rurik Voss entry rather than creating a second character. Retain and refine Elandor Rurik's fuller profile.
  - `Captain_Ruriks_Request_Session_0-1.md`: Use Elandor Rurik consistently as the quest giver and owner of The Rusty Anchor.
  - `Quests_Player_Decisions_Impacts.md`: Track all Rurik relationships, rewards, debts, ship consequences, and quest outcomes under Elandor Rurik's single identity.
  - `Early_Sessions_Plan_Sessions_0_to_5.md`: Replace any shortened or conflicting identity with Elandor Rurik.
  - Character clarification:
    - Elandor is a veteran independent ship captain and tavern proprietor.
    - He is **semi-retired from routine sailing**, not fully retired. He still owns his ship and accepts selective, profitable, or sensitive cargo contracts, which explains the medallion delivery.
    - "Captain" remains an earned title and common form of address.
    - He is not a member of the Voss ruling family.
    - Preserve his black eyepatch, weathered sailor appearance, blunt but fair temperament, concern for his crew and livelihood, minor past smuggling connections, and friendly relationship with Lirael "Silverthorn."
- **Cross-reference and validation work:**
  - Search for `Captain Rurik Voss`, `Rurik Voss`, `Captain Rurik`, `Elandor Rurik`, `Blackscale`, and `The Rusty Anchor`.
  - Ensure only one active proprietor and one starter-quest giver exists.
  - Ensure references to his ship and selective cargo work do not describe him as completely retired.
  - Preserve Voss-family intrigue through Elara Voss and Lirael "Silverthorn," not through Rurik.
- **Canon decisions required:** None for this proposal. The user authorized corrective consolidation and has no attachment to the duplicate AI-generated identities.
- **Status:** Decision approved; awaiting completion and approval of the full Batch B implementation set.


### Batch B-06 — Aether terminology and Veyne's organization

- **Requested outcome:** Establish one vocabulary for the realm, its people, its technology, and Veyne's secret organization while removing accidental AI-generated variants.
- **Affected files:**
  - all canon, city, NPC, quest, session, encounter, navigation, and campaign-reference files using Aether-related terminology
- **Exact terminology:**
  - **Aetheron** — the world or realm where the advanced civilization resides and where beacon-harvested magic is sent. The term may also describe that civilization collectively when the meaning is clear.
  - **Aetheronian** — singular adjective or person associated with Aetheron.
  - **Aetheronians** — the people of Aetheron.
  - **Aetherite** — the magical crystal material and the broad technological tradition constructed from or powered by that material.
  - **Aetherite crystal/orb** — a physical crystal device, whether rune-inscribed or unmarked.
  - **Aetherite technology** — weapons, beacons, gates, power systems, and other devices created through Aetheronian crystal engineering.
  - **Aetherbound** — retire as the in-world name of Veyne's organization. It may remain temporarily as the repository or campaign working title until a separate title decision is made.
  - **Veyne's organization** — use this neutral description in canon until an intentional secret-society name is selected. Do not invent another faction name during cleanup.
  - **Aetherian / Aetherians** — retire as undefined accidental variants. Replace with Aetheronian, Aetheronians, Aetherite, or Aetheron according to context.
  - **Aetherite people / the Aetherites** — retire when referring to a population. Aetherite describes material or technology, not ethnicity or nationality.
- **Exact edits by usage:**
  - Replace “Aetherian home world” with **Aetheron**.
  - Replace “Aetherian people” with **Aetheronians**.
  - Replace “Aetherian weapon,” “Aetherian crystal,” or similar technological wording with **Aetherite weapon**, **Aetherite crystal**, or **Aetherite technology**.
  - Replace “created by the Aetherites” with **created by the Aetheronians**.
  - Replace in-world references to an “Aetherbound faction” with **Veyne's organization** until it receives an approved name.
  - Preserve the distinction that using Aetherite technology does not make a person Aetheronian.
- **Veyne relationship to Aetheron:**
  - Lord Cassian Veyne is the primary campaign antagonist and leader of the unnamed secret organization pursuing his goals.
  - Veyne has physically traveled to Aetheron using the approved three-crystal Aetherite travel array.
  - His access to Aetheron and Aetherite technology gives him genuine knowledge beyond ordinary Elyndrian scholars.
  - His organization is not automatically synonymous with the Aetheronian civilization and should not be described as representing all Aetheronians.
  - The exact Aetheronian individuals, institutions, or factions interacting with Veyne may be developed later without changing this terminology standard.
- **Cross-reference and validation work:**
  - Search case-insensitively for Aetheron, Aetheronian, Aetheronians, Aetherite, Aetherian, Aetherians, Aetherites, and Aetherbound.
  - Correct each occurrence according to meaning rather than performing a blind global replacement.
  - Synchronize terminology in the World Bible, geography, NPC database, quest files, early-session plan, city profiles, stat blocks, and campaign index.
  - Keep player-facing language vague where the characters have not yet learned the true names.
- **Canon decisions required:** A permanent name for Veyne's secret organization may be selected later. Until then, “Veyne's organization” is the approved neutral wording.
- **Status:** Terminology approved; organization name intentionally deferred. Awaiting implementation with the rest of Batch B.

## Required Proposal Format

### Change title

- **Requested outcome:**
- **Affected files:**
  - `Exact_File_Name.md`
- **Exact edits by file:**
  - `Exact_File_Name.md`: Describe the precise addition, replacement, removal, or rename.
- **Cross-reference and validation work:**
- **Canon decisions required:** None / list the decisions
- **Status:** Awaiting approval

## Current Editable Markdown Inventory

### Governance and navigation

- `GOVERNANCE.md`
- `AGENTS.md`
- `SKILL.md`
- `README.md`
- `Campaign_Index_and_Quick_Reference.md`
- `Pending_Changes.md`

### Core campaign documents

- `DnD_Campaign_World_Bible.md`
- `World_Geography.md`
- `NPC_Backstory_Personality_file.md`
- `Quests_Player_Decisions_Impacts.md`
- `Enemy_Encounters_Stat_Blocks.md`
- `Captain_Ruriks_Request_Session_0-1.md`
- `Early_Sessions_Plan_Sessions_0_to_5.md`

### City profiles

- `Ravensport_City_Profile.md`
- `Deepanvil_City_Profile.md`
- `Faerindel_City_Profile.md`
- `Ironforge_City_Profile.md`

### Guidelines

- `City_Creation_Guidelines.md`
- `Guideline_Battle_Stat_Block_Management.md`
- `Guideline_NPC_Character_Creation.md`
- `Guideline_Quest_Creation.md`
- `Guideline_World_Geography_Map_Creation.md`
- `Guideline_World_Update_Change_Management.md`

### Historical logs

Files matching `Pending_Changes_Archived_*.md` are historical records. They are not active proposal files and should not be edited except to correct misleading archive labeling or preserve readability.

## Approval and Archival

After the user approves an exact proposal or documented batch:

1. Apply the approved changes.
2. Create the next numbered `Pending_Changes_Archived_XX.md` record with the approved scope and implementation result.
3. Reset this file so **Active Proposed Changes** again reads `_No active proposals._`.
