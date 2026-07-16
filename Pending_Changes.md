---
status: Active Reference
authority: Proposed Change Staging
version: 3.4
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


## Batch C — Playability and template completion

### Batch C-01 — Basic Services: Ravensport and Deepanvil

- **Requested outcome:** Add practical, table-ready Basic Services sections to Ravensport and Deepanvil while clarifying how permanently improved physical materials and tools function inside dead zones.
- **Affected files:**
  - `Ravensport_City_Profile.md`
  - `Deepanvil_City_Profile.md`
  - `DnD_Campaign_World_Bible.md`
  - any session, quest, encounter, or equipment reference that incorrectly treats dead zones as undoing permanent physical changes
- **Exact edits by file:**

  - `Ravensport_City_Profile.md`: Add a **Basic Services** section using the following approved framework:
    - **Lodging and meals:** Widely available at every price level. Cheap lodging is concentrated around the docks and Shrouded Wards; comfortable inns serve merchants and travelers; expensive lodging is found near the Grand Bazaar and Noble Hill. Prices rise during major gate arrivals, festivals, or shipping delays.
    - **Mundane equipment and repairs:** Common weapons, armor, adventuring supplies, ship equipment, clothing, and tools are readily available. Specialized military equipment, siege gear, gate-security devices, and official uniforms require permits or government authorization.
    - **Healing and medical care:** Mundane physicians, apothecaries, temple healers, and magical healing are available. Minor healing is accessible to paying customers. Restoration, curse removal, resurrection, and treatment of unusual planar conditions require substantial payment, official approval, a wealthy patron, or access to senior healers.
    - **Temples and spiritual assistance:** Multiple recognized faiths maintain temples, shrines, and chapels because of the city's diverse population. Ordinary worship and counseling are open to visitors. Dangerous rituals, resurrection, divine investigations, and ceremonies involving unknown planar beings receive government scrutiny.
    - **Transportation and stabling:** Stables, wagon yards, river barges, ships, couriers, and hired carriages are common. Travel through the dimensional gate requires identification, inspection, declared cargo, tariffs, and authorization from gate officials.
    - **Banking, currency exchange, and secure storage:** Merchant banks, guild vaults, money changers, letters of credit, and secured warehouses are widely available. Large deposits, foreign currency, dimensional goods, magical artifacts, and Aetherite technology may be inspected or reported.
    - **Messengers and information:** Local runners, guild couriers, ship messengers, public notices, tavern rumors, and merchant information networks are easy to find. Magical communication is available but expensive. Messages involving gate security or restricted technology may be monitored or refused.
    - **Legal help, permits, and government offices:** Advocates, scribes, translators, customs officials, and permit offices operate throughout the city. Common needs include trade licenses, cargo declarations, gate-travel documents, weapon permits, and claims involving damaged or stolen shipments.
    - **Hiring labor, guides, or guards:** Sailors, dockworkers, caravan hands, translators, local guides, licensed guards, mercenaries, and adventurers can be hired openly. Active city guards and Iron Talons cannot be privately hired.
    - **Magical services:** Spell components, scrolls, identification, minor enchantment, magical repairs, and common magical services are available through licensed practitioners. Teleportation, planar travel, powerful divination, dangerous summoning, and experimentation near the gate are heavily restricted.
    - **Defining limitation:** Ravensport's problem is not availability. Almost anything can be found, but valuable, magical, foreign, or dimensional goods attract permits, tariffs, inspections, and official attention.

  - `Deepanvil_City_Profile.md`: Add a **Basic Services** section using the following approved framework:
    - **Lodging and meals:** Clan halls, miners' inns, bunkhouses, and practical taverns serve residents and visitors. Meals are filling but depend heavily on imported grain, produce, meat, and spices. Visitors without clan or trade connections pay more for premium lodging.
    - **Mundane equipment and repairs:** Availability and quality are exceptional. Deepanvil uses advanced engineering, standardized parts, and tools manufactured from magically perfected materials outside the dead zone. Repairs and routine work are often faster and cheaper than in magic-dependent cities.
    - **Healing and medical care:** Deepanvil has highly trained surgeons, herbalists, bone-setters, prosthetic specialists, and mine-rescue physicians. Active magical healing does not function inside the dead zone, but magically perfected surgical tools, materials, prosthetic components, medicines, and other permanent physical improvements remain usable.
    - **Temples and spiritual assistance:** Temples, ancestor halls, and shrines remain active as places of worship, mourning, counsel, and community. Clergy retain their learning and social authority, but cannot perform active magical miracles without an approved resonance source.
    - **Transportation and stabling:** Mechanical lifts, rail carts, freight elevators, wagons, pack animals, and secured mountain routes are common. Infrastructure is highly reliable because it was designed to function without active magic.
    - **Banking, currency exchange, and secure storage:** Clan vaults, trade-company accounts, gem exchanges, sealed warehouses, and precision mechanical lockboxes are widely available. Deepanvil is exceptionally secure against magical intrusion because outside magical access fails within the zone.
    - **Messengers and information:** Runners, signal bells, mechanical message tubes, coded lanterns, written notices, and caravan couriers replace magical communication. Messages may be transferred to magical couriers after leaving the zone.
    - **Legal help, permits, and government offices:** Mining claims, excavation permits, engineering ownership, labor disputes, clan contracts, and safety violations are handled through the Mining Council and clan representatives. Outsiders often need a local sponsor for restricted mines or workshops.
    - **Hiring labor, guides, or guards:** Miners, engineers, mechanics, guards, tunnel guides, demolition experts, rescue crews, and specialized repair teams are readily available. Skilled labor is respected and priced according to expertise.
    - **Magical services:** Active spellcasting and active enchantment services are not normally available inside the dead zone. Items may be taken outside the zone for enchantment, permanent magical manufacturing changes, or magical treatment, then returned for ordinary use when their benefits no longer require continuing magical energy.
    - **Defining strength:** Deepanvil is not worse because active magic is unavailable. Its people have become better at engineering, maintenance, medicine, rescue, manufacturing, and mundane logistics. What magic cannot continuously operate, Deepanvil replaces with superior physical design and practiced expertise.

  - `DnD_Campaign_World_Bible.md`: Clarify the approved distinction between suppression of active magic and preservation of completed physical changes:
    - Dead zones suppress effects that require magical energy to activate, continue, communicate, move, repair, or sustain themselves.
    - A completed magical process does not reverse merely because its result enters a dead zone.
    - Permanent physical alterations remain when they have become ordinary properties of the affected material or body and no longer require ongoing magical energy.
    - Examples include magically refined alloys, physically hardened or lightened materials, precision-shaped parts, permanently sharpened or balanced tools, reinforced structures, and completed physical transformations.
    - Active enchantments remain suppressed. A self-moving tool, flaming weapon, levitating platform, extradimensional container, magical communication device, automatic repair effect, or continuously empowered enhancement does not function merely because it was created outside the zone.
    - When classification is uncertain, ask whether the benefit is now a physical property or still requires continuing magical power. Physical properties remain; ongoing magical functions are suppressed.
    - This clarification narrows, rather than removes, the rule that magic items are normally suppressed inside dead zones.

- **Cross-reference and validation work:**
  - Review descriptions of Deepanvil technology, medicine, tools, manufacturing, infrastructure, and trade so the city is not presented as primitive or disadvantaged.
  - Distinguish magically manufactured mundane equipment from actively enchanted equipment.
  - Preserve the approved Resonance Orb and beacon-core exceptions for active magic.
  - Keep Ravensport's central service limitation focused on regulation and inspection.
- **Canon decisions required:** None. Ravensport Basic Services and the revised Deepanvil interpretation were approved during Batch C discussion.
- **Status:** Decision approved; remaining city Basic Services are still under discussion.


### Batch C-02 — Basic Services: Faerindel Gate City

- **Requested outcome:** Add table-ready Basic Services to Faerindel while establishing that a highly magical gate city also maintains advanced technological and nonmagical systems because anti-magic defenses are part of gate security.
- **Affected files:**
  - `Faerindel_City_Profile.md`
  - `DnD_Campaign_World_Bible.md`
  - any gate-city, defense, service, session, or encounter reference that assumes a magical gate city relies only on active magic
- **Exact edits by file:**

  - `Faerindel_City_Profile.md`: Add a **Basic Services** section using the following approved framework:
    - **Lodging and meals:** Guest houses, living-tree inns, private retreats, and communal lodges are available. Food is fresh and heavily based on local agriculture, fruit, herbs, game, and imported delicacies. Respectful visitors are welcomed, while disruptive or environmentally careless travelers may be refused service.
    - **Mundane equipment and repairs:** Faerindel has an above-average selection of mundane adventuring equipment, bows, armor, tools, replacement parts, medical supplies, and gate-compatible gear. Local goods emphasize precision, low weight, durability, and graceful design. Dwarven industrial equipment and heavy machinery are imported, but commonly stocked because the gate district requires dependable nonmagical backups.
    - **Technological services:** Engineers, artificers, mechanics, ward technicians, and specialist craftspeople maintain physical locks, mechanical barriers, signal systems, inspection devices, transport mechanisms, and other systems designed to function during anti-magic activation. Technology is treated as a necessary partner to magic rather than an inferior substitute.
    - **Healing and medical care:** Herbalists, physicians, surgeons, druids, and magical healers provide excellent care. Gate-security stations maintain mundane triage rooms, surgical tools, medicines, and evacuation procedures that remain functional when anti-magic fields are active. Powerful restoration, resurrection, or transformation requires approval from senior civic or religious authorities.
    - **Temples and spiritual assistance:** Sacred groves, ancestral shrines, nature sanctuaries, and temples provide worship, counseling, funerals, and spiritual guidance. Public areas welcome outsiders, but ancient or sensitive sacred sites require invitation. Clergy serving near the gate are trained to continue nonmagical care and leadership when divine spell expression is suppressed.
    - **Transportation and stabling:** Forest guides, riding animals, wagons, river transport, and magically assisted local travel are available. The gate complex relies on physical carts, lifting systems, secured passages, and trained handlers whenever anti-magic defenses are active. Gate travel remains strictly inspected and documented.
    - **Banking, currency exchange, and secure storage:** Trade houses handle coin exchange, letters of credit, valuables, and dimensional currency. Secure storage combines magical seals and living wards with high-quality physical vaults, mechanical locks, and nonmagical accounting systems. Unknown planar objects may be quarantined before acceptance.
    - **Messengers and information:** Couriers, trained birds, ranger networks, public notices, magical communication, scholars, and lorekeepers are available. Gate operations maintain redundant nonmagical signals and runners because magical communication can be deliberately suppressed during an emergency.
    - **Legal help, permits, and government offices:** Council scribes, interpreters, trade officials, and advocates assist with gate documents, trade permissions, land access, magical research, technology importation, and harvesting rights. Foreigners may need a recognized local sponsor for sensitive requests.
    - **Hiring labor, guides, or guards:** Rangers, trackers, herbalists, translators, craftspeople, mechanics, porters, and wilderness escorts may be hired. Active Wardens cannot be privately employed, but retired Wardens and licensed guides are available.
    - **Magical services:** Enchantment, identification, healing, magical tailoring, scroll work, protective charms, druidic services, and magical research are highly developed. The city therefore leans toward high-quality magical goods, but gate-security requirements also create unusually strong demand for nonmagical alternatives.
    - **Anti-magic limitation:** Permanent and emergency anti-magic fields protect the dimensional gate from magical invasion, hostile teleportation, summoned creatures, and incoming spell effects. Magical items and active spell effects are suppressed while within an activated field, so gate staff, merchants, healers, guards, and transport workers maintain nonmagical procedures and equipment.
    - **Restricted practices:** Necromancy, uncontrolled summoning, destructive experimentation, interference with gate wards, and magic that damages natural systems are prohibited or heavily restricted.
    - **Defining character:** Faerindel is not merely a magical city. It is a mature gate city whose people understand that security may require magic to be shut off. Its services combine exceptional magic with above-average mundane goods and technology capable of operating during anti-magic conditions.

  - `DnD_Campaign_World_Bible.md`: Clarify the general gate-city service and defense principle:
    - Major dimensional gate cities maintain anti-magic fields, corridors, chambers, or emergency suppression zones around their gates.
    - These defenses exist to stop hostile spellcasting, magical creatures, summoned reinforcements, teleportation, and magical attacks emerging through the gate.
    - Anti-magic coverage is concentrated around the gate complex and can include permanent controlled areas plus larger emergency fields activated during a threat. It does not normally suppress the entire city.
    - Because gate personnel must operate during suppression, gate cities invest heavily in mundane weapons, physical barriers, mechanical systems, conventional medicine, runners, signals, secure locks, and other nonmagical infrastructure.
    - Gate cities may have excellent magical markets while also maintaining better mundane equipment and technology than ordinary magical settlements.
    - Items crossing an anti-magic inspection area temporarily lose active magical functions but recover when removed, unless separately damaged or drained by another effect.

- **Cross-reference and validation work:**
  - Review descriptions of Faerindel's gate defenses, services, shops, Wardens, transportation, healing, and communication.
  - Do not portray technology and magic as mutually exclusive.
  - Preserve Faerindel's cultural emphasis on responsible magic, nature, and trust.
  - Ensure anti-magic defenses are localized to the gate complex or activated emergency areas rather than accidentally turning all of Faerindel into a dead zone.
  - Apply the same general gate-city principle later to Ravensport and Ironforge while preserving their different cultures and service strengths.
- **Canon decisions required:** None. The mixed high-magic, technological, and nonmagical service model was approved during Batch C discussion.
- **Status:** Decision approved; Ironforge Basic Services remain under discussion.


### Batch C-03 — Basic Services: Ironforge Gate City

- **Requested outcome:** Add table-ready Basic Services to Ironforge while distinguishing dwarven magical practice from Faerindel's broader arcane and nature-based traditions.
- **Affected files:**
  - `Ironforge_City_Profile.md`
  - `DnD_Campaign_World_Bible.md`
  - any gate-city, dwarven-magic, equipment, defense, service, session, or encounter reference involving Ironforge
- **Exact edits by file:**

  - `Ironforge_City_Profile.md`: Add a **Basic Services** section using the following approved framework:
    - **Lodging and meals:** Clan guest halls, miners' inns, military lodges, merchant housing, and private rooms are widely available. Meals favor meat, bread, root vegetables, strong drink, and imported produce. Travelers connected to a clan, guild, military unit, or trade company receive better accommodations and prices.
    - **Mundane equipment and repairs:** Availability is exceptional. Weapons, armor, tools, mining equipment, locks, wagons, machinery, and replacement parts are produced locally. Common repairs are fast and affordable; masterwork, experimental, or military work requires access to a respected smith, engineer, or clan workshop.
    - **Technological services:** Ironforge maintains advanced mechanical lifts, rail systems, industrial machinery, siege engines, inspection devices, ventilation systems, and physical gate defenses. Engineers can design or modify complex equipment, but military-grade plans, proprietary clan designs, and gate-security systems are restricted.
    - **Healing and medical care:** Physicians, surgeons, alchemists, prosthetic specialists, temple healers, and magical practitioners are available. Gate and mine facilities maintain mundane emergency hospitals capable of operating during anti-magic activation.
    - **Temples and spiritual assistance:** Clan shrines, ancestor halls, forge temples, and major religious sanctuaries are common. Priests provide counsel, rites, healing, funerals, and blessings connected to craft, duty, clan, and defense. Active divine magic is suppressed inside activated anti-magic areas.
    - **Transportation and stabling:** Freight lifts, underground rail carts, wagons, pack animals, mountain roads, and dimensional gate transport are available. Heavy cargo can be moved more efficiently here than in most cities. Gate cargo undergoes inspection, weighing, documentation, and security review.
    - **Banking, currency exchange, and secure storage:** Ironforge maintains exceptionally secure clan vaults, gem exchanges, trade banks, bonded warehouses, and physical storage facilities. Access to the most secure or prestigious services often depends on clan sponsorship, reputation, or a commercial contract.
    - **Messengers and information:** Runners, signal bells, speaking tubes, mechanical message systems, guild couriers, and magical communication are available. The gate complex, mines, and defensive districts maintain redundant nonmagical networks for emergencies.
    - **Legal help, permits, and government offices:** Clan advocates, contract scribes, trade officials, mining registrars, engineering inspectors, and gate authorities handle disputes and licenses. Permits are required for mining claims, heavy machinery, explosives, gate cargo, military equipment, and restricted magical materials.
    - **Hiring labor, guides, or guards:** Miners, smiths, engineers, mechanics, caravan guards, mountain guides, excavation crews, and mercenaries are readily available. Highly skilled workers may refuse jobs that violate clan contracts, professional honor, or city security.
    - **Magical services:** Rune work, enchantment, identification, magical repair, weapon enhancement, armor reinforcement, ward construction, ammunition enhancement, powered tools, and artifact study are highly developed.
    - **Dwarven magical tradition:** Ironforge magic is usually applied through crafted objects and mechanical systems. Spellcasters most often support weapons, armor, tools, fortifications, artillery, vehicles, mining equipment, and industrial machinery rather than treating spellcasting as a separate art.
    - **Common examples of Ironforge magic:** Rune-enhanced blades, reinforced armor, guided ammunition, impact-amplifying hammers, warded shields, heat-controlled forges, magically assisted targeting systems, powered excavation tools, and defensive mechanisms that combine physical engineering with enchantment.
    - **Operational philosophy:** Ironforge equipment should remain useful when magic is suppressed. Enchantments enhance a strong physical design; they do not replace the underlying weapon, tool, lock, vehicle, or defensive mechanism.
    - **Anti-magic readiness:** The Gate Heart contains permanent inspection areas and emergency anti-magic fields. Ironforge compensates with heavy doors, mechanical traps, physical artillery, mundane weapons, armored troops, and systems that continue operating without magic.
    - **Defining limitation:** Ironforge can build or repair almost anything, but access to its best work depends on reputation, clan relationships, permits, and whether the project threatens dwarven security, trade interests, or proprietary knowledge.
    - **Defining distinction:** Faerindel treats magic as a broad expression of nature, learning, healing, and enchantment. Ironforge treats magic primarily as a force to be engineered into reliable weapons, defenses, tools, and machines.

  - `DnD_Campaign_World_Bible.md`: Add the following cultural distinction:
    - Dwarven magical practice in Ironforge is primarily **integrated magic**: runes, enchantments, and spell effects are built into physical equipment and engineered systems.
    - Dwarven crafters generally begin with a mechanically sound weapon, tool, structure, or machine and then use magic to improve power, accuracy, durability, control, efficiency, or defensive value.
    - This differs from Faerindel's broader traditions of nature magic, direct spellcraft, healing, living architecture, and artistic enchantment.
    - Ironforge's best creations remain functional mundane objects when anti-magic fields suppress their enhancements.

- **Cross-reference and validation work:**
  - Review Ironforge shops, services, defenses, military equipment, gate operations, and encounter descriptions.
  - Ensure dwarven magic is presented as supporting mechanics and craftsmanship rather than replacing them.
  - Preserve overlap where appropriate: Ironforge still has healers, priests, scholars, and direct spellcasters, but its strongest cultural emphasis is engineered magical equipment.
  - Keep Ironforge distinct from Deepanvil: Ironforge uses both magic and machinery; Deepanvil specializes in perfected physical systems that function continuously without active magic.
- **Canon decisions required:** None. Ironforge Basic Services and its integrated weapon-and-mechanics magical tradition were approved during Batch C discussion.
- **Status:** Decision approved. Basic Services are now approved for all four city profiles.


### Batch C-04 — Trade, supply, and black-market status for the four major cities

- **Requested outcome:** Add concise, play-focused trade and black-market information to Ravensport, Deepanvil, Faerindel, and Ironforge without creating a detailed economic simulation.
- **Affected files:**
  - `Ravensport_City_Profile.md`
  - `Deepanvil_City_Profile.md`
  - `Faerindel_City_Profile.md`
  - `Ironforge_City_Profile.md`
  - `World_Geography.md`
  - relevant quest, session, NPC, and encounter files that depend on trade routes, shortages, smuggling, or restricted goods
- **General format for each city:**
  - **Major exports:** 3–6 goods or services that explain why the city matters.
  - **Major imports:** 3–6 necessities or specialties the city depends upon.
  - **Restricted goods:** Items requiring permits, inspection, sponsorship, or government approval.
  - **Black-market status:** Whether illicit trade is open, hidden, specialized, clan-controlled, or aggressively suppressed.
  - **Current supply pressure:** One practical shortage, bottleneck, or dispute that can generate rumors and quests.

#### Ravensport — Trade and Supply

- **Major exports:**
  - Re-exported dimensional and continental goods distributed through the docks, roads, river, and gate network.
  - Fish, preserved seafood, ship supplies, rope, sailcloth, and processed dockside goods.
  - Warehousing, cargo brokerage, customs services, banking, letters of credit, and caravan coordination.
  - Finished consumer goods assembled from imported materials.
  - Information, translation, transportation, and gate-navigation services.
- **Major imports:**
  - Food from surrounding farms and inland trade routes.
  - Ore, metalwork, machinery, weapons, and tools from dwarven cities.
  - Enchanted goods, medicines, herbs, fine textiles, and magical services from Faerindel.
  - Timber, stone, livestock, fuel, luxury goods, and dimensional cargo.
- **Restricted goods:**
  - Aetherite crystals and technology.
  - Unregistered dimensional artifacts or living specimens.
  - Military weapons, siege equipment, gate-security devices, and official uniforms.
  - Dangerous magical components, summoning materials, cursed objects, and undeclared planar cargo.
  - Forged travel documents, gate permits, customs seals, and restricted maps.
- **Black-market status:**
  - Large, organized, and active.
  - Concentrated in the Shrouded Wards, docks, private warehouses, corrupt brokerage offices, and false-front shipping companies.
  - Common illicit trade includes stolen cargo, forged gate papers, undeclared dimensional goods, restricted magic, Aetherite-related objects, information, and bribed inspections.
  - City authorities suppress visible crime but cannot eliminate smuggling without disrupting legitimate trade.
- **Current supply pressure:**
  - Gate inspections and increased security have created cargo backlogs, rising warehouse fees, and opportunities for bribery, theft, and false documentation.
- **Play identity:**
  - Almost anything can be bought or moved through Ravensport, legally or illegally, but every valuable transaction leaves paperwork, witnesses, debts, or official attention.

#### Deepanvil — Trade and Supply

- **Major exports:**
  - Rare ores, refined metals, gemstones, and specialty alloys.
  - Precision tools, modular replacement parts, mining equipment, pumps, lifts, drills, and mechanical safety systems.
  - Masterwork mundane weapons, armor components, locks, vault mechanisms, and industrial hardware.
  - Prosthetics, surgical instruments, rescue equipment, and durable goods designed for use without active magic.
  - Engineering services, mine planning, and dead-zone-compatible infrastructure.
- **Major imports:**
  - Grain, meat, produce, spices, preserved food, and clean agricultural supplies.
  - Timber, cloth, leather, paper, lamp oils, medicines, herbs, and alchemical ingredients.
  - Magically perfected raw materials or components manufactured outside the dead zone.
  - Luxury goods and cultural items unavailable underground.
- **Restricted goods:**
  - Mining explosives, demolition equipment, restricted drilling systems, and military-grade mechanisms.
  - Unregistered mining claims, geological surveys, and proprietary engineering plans.
  - Aetherite devices, resonance orbs, and technology capable of enabling active magic inside the dead zone.
  - Sacred clan relics and materials taken from sealed depths.
- **Black-market status:**
  - Smaller than Ravensport's but highly specialized and difficult for outsiders to access.
  - Operates through clan connections, corrupt foremen, freight manifests, abandoned tunnels, and private workshops.
  - Common illicit trade includes stolen ore, falsified claim records, restricted explosives, proprietary designs, unregistered mechanisms, and magical items brought into the zone where their active properties cannot be easily tested.
  - Smuggling is treated seriously because unsafe goods can cause cave-ins, industrial disasters, or clan conflict.
- **Current supply pressure:**
  - Deepanvil depends on regular surface shipments of food, medicine, timber, and cloth. Road disruption or caravan losses quickly raise prices and strain poorer districts.
- **Play identity:**
  - Deepanvil sells the finest practical equipment and engineering in Elyndria, but its dependence on imported necessities makes its trade routes strategically vital.

#### Faerindel — Trade and Supply

- **Major exports:**
  - Enchanted textiles, protective clothing, fine bows, precision light weapons, and artistic magical goods.
  - Medicines, herbs, potions, antidotes, restorative compounds, and nature-based alchemical products.
  - Scrolls, scholarly works, magical research, identification services, and carefully licensed enchantments.
  - Fine woodwork, living-wood crafts, jewelry, and sustainably harvested rare materials.
  - Gate-navigation knowledge, translation, and specialized planar consultation.
- **Major imports:**
  - Refined metals, heavy tools, machinery, structural components, and nonmagical gate-security equipment.
  - Stone, industrial materials, dwarven locks, physical vault components, and military hardware.
  - Foreign foods, luxury goods, rare inks, crystals, laboratory materials, and dimensional curiosities approved for study.
- **Restricted goods:**
  - Poached sacred plants, animals, wood, or remains.
  - Necromantic materials, uncontrolled summoning tools, corruptive artifacts, and objects that damage natural systems.
  - Unregistered planar organisms, invasive species, forbidden enchantments, and research removed from protected archives.
  - Devices intended to bypass living wards, gate inspections, or anti-magic controls.
- **Black-market status:**
  - Quiet, selective, and relationship-based rather than openly criminal.
  - Operates through private collectors, disgraced scholars, unauthorized harvesters, hidden research circles, and traders who conceal restricted goods inside legitimate magical commerce.
  - Common illicit trade includes forbidden enchantments, poached natural materials, unregistered planar specimens, memory-altering magic, protected lore, and technology that violates environmental or gate restrictions.
  - Outsiders rarely find it without a trusted intermediary.
- **Current supply pressure:**
  - Growing demand for dwarven machinery and nonmagical gate-security systems is creating political tension between practical reformers and traditionalists who fear technological dependence.
- **Play identity:**
  - Faerindel's illicit trade is not the largest, but its contraband is often rare, culturally sensitive, magically dangerous, or tied to forbidden knowledge.

#### Ironforge — Trade and Supply

- **Major exports:**
  - Weapons, armor, shields, ammunition, tools, mining equipment, and heavy machinery.
  - Siege engines, defensive mechanisms, mechanical gate systems, locks, vaults, and industrial infrastructure.
  - Refined metals, specialty alloys, cut gems, rune-enhanced equipment, and integrated magical machinery.
  - Engineering expertise, military contracts, fortification design, and large-scale repair services.
- **Major imports:**
  - Grain, produce, livestock, timber, cloth, leather, medicines, herbs, oils, and alchemical reagents.
  - Fine magical materials, living components, rare woods, and enchantment supplies from Faerindel.
  - Dimensional ores, experimental technologies, luxury goods, and specialist knowledge passing through gate trade.
- **Restricted goods:**
  - Military-grade weapons, siege plans, prototype machinery, gate-defense systems, and clan-owned designs.
  - High explosives, restricted runes, enchanted ammunition, armor-piercing devices, and unregistered dimensional metals.
  - Sacred relics, sealed historical records, and components tied to the Gate Heart.
- **Black-market status:**
  - Heavily controlled and usually hidden behind clan, guild, military, or contracting relationships.
  - Common illicit trade includes stolen weapons, counterfeit maker's marks, proprietary engineering plans, restricted runes, unregistered explosives, gate salvage, and relic trafficking.
  - Street criminals handle minor theft, but serious contraband usually involves someone with workshop, clan, military, or warehouse access.
  - Penalties are severe because stolen designs can threaten both trade dominance and city defense.
- **Current supply pressure:**
  - Food, timber, medicine, and other surface necessities remain vulnerable to mountain-route disruption, while military production competes with civilian demand for metals and skilled labor.
- **Play identity:**
  - Ironforge can supply armies and industries, but its most advanced products are controlled through reputation, contracts, clan authority, and security clearance.

- **Cross-reference and validation work:**
  - Use `World_Geography.md` to confirm that the named roads, waterways, mountain routes, and gate connections support these trade relationships.
  - Keep lists high-level and actionable; do not add trade tonnage, detailed taxation tables, or commodity-price simulations.
  - Use shortages and black-market categories as sources for rumors, thefts, escorts, investigations, and political disputes.
  - Preserve the approved distinction between legal Aetherite scholarship or possession and unlicensed, concealed, or weaponized Aetherite trade.
  - Ensure each city's black market reflects its culture rather than repeating the same criminal structure.
- **Canon decisions required:** None at this stage. Exact named smugglers, criminal organizations, and individual trade disputes may be added later when they become relevant to play.
- **Status:** Approved for staging under the user's delegated authority for high-level trade and black-market development.


### Batch C-05 — Gate-city daily life and current tensions

- **Requested outcome:** Establish a consistent, centuries-old gate-city culture in which dimensional danger is a normal fact of life, heavy security is concentrated within the Heart, and current tensions arise from pressure within cooperation rather than from ordinary citizens opposing gate defense.
- **Affected files:**
  - `Ravensport_City_Profile.md`
  - `Faerindel_City_Profile.md`
  - `Ironforge_City_Profile.md`
  - `Deepanvil_City_Profile.md` where gate-city comparison or regional cooperation is discussed
  - `DnD_Campaign_World_Bible.md`
  - `World_Geography.md`
  - relevant NPC, quest, session, encounter, and starter material
- **Exact edits by file:**

  - `DnD_Campaign_World_Bible.md`: Add the following shared gate-city canon:
    - Each major dimensional gate is contained inside a heavily fortified inner district commonly called the **Heart**.
    - Heavy inspections, anti-magic screening, cargo controls, restricted access, and military oversight are concentrated within the Heart and at actual gate-transit points.
    - Ordinary citizens do not experience gate-level inspections while moving through normal residential, commercial, religious, industrial, or civic districts.
    - Entry into the Heart requires identification, sponsorship or official purpose, inspection of people and cargo, declaration of restricted magic or technology, and compliance with gate-security procedures.
    - Gate cities have operated for centuries. Their populations treat dimensional danger as a permanent fact of life rather than a new or universally traumatic condition.
    - Residents commonly know alarm signals, emergency routes, shelter procedures, traffic closures, and the difference between routine containment activity and a serious breach.
    - Most long-term residents have heard beasts, hostile beings, weapons, impacts, or unnatural sounds from inside the Heart as defenders contain attempted incursions.
    - These events are serious but socially normalized. People pause, listen for the official follow-up signal, adjust work or travel when needed, and resume ordinary life once containment is confirmed.
    - Human, dwarven, and elven powers cooperate because no people has enough manpower, magic, technology, logistics, or resources to defend every gate alone.
    - Legitimate governments may compete over contracts, trade, command authority, costs, and defensive methods, but they consider open warfare and deliberate gate sabotage existentially irresponsible.
    - Intentional weakening of gate defenses is treated as a civilization-level threat and normally points to Veyne's organization, apocalyptic extremists, hostile planar forces, magical control, deception, or similarly exceptional causes.

  - `Ravensport_City_Profile.md`: Add a **Daily Life and Current Tensions** section reflecting:
    - Ordinary city districts remain busy, commercial, cosmopolitan, and comparatively free of gate-level intrusion.
    - Residents are accustomed to distant alarms, military movement toward the Heart, temporary road closures, and the sounds of contained incursions.
    - Current tensions focus on cargo backlogs, unequal access to contracts, warehouse costs, dock labor disputes, corruption, favoritism, and who receives priority through the Heart.
    - Smuggling and forged permits are common criminal concerns, but ordinary criminals avoid directly weakening gate defenses.
    - A change in the pattern of incursions—greater frequency, coordination, intelligence, unfamiliar creatures, or knowledge of the Heart's layout—is considered genuinely alarming.

  - `Faerindel_City_Profile.md`: Add a **Daily Life and Current Tensions** section reflecting:
    - Daily life combines living architecture, ritual, study, agriculture, craft, and routine gate readiness.
    - Citizens accept the Heart's security and anti-magic procedures as necessary, even in a highly magical culture.
    - Current tensions focus on how much technology to integrate, who may access restricted research, whether trade growth threatens cultural or environmental responsibilities, and how much authority gate officials should exercise over scholars and visiting mages.
    - Traditionalists and reformers disagree over methods, not over whether the gate must be defended.
    - Unusual changes in planar behavior, ward responses, or creature coordination are treated as serious threats.

  - `Ironforge_City_Profile.md`: Add a **Daily Life and Current Tensions** section reflecting:
    - Work, clan obligations, military readiness, engineering, trade, and gate defense are woven into ordinary life.
    - Residents accept drills, freight redirection, sealed passages, and emergency activation of mechanical and anti-magic defenses as routine civic responsibilities.
    - Current tensions focus on military versus civilian production, clan control of contracts, proprietary designs, skilled-labor shortages, access to the Gate Heart, and whether foreign partners receive too much or too little technical access.
    - Dwarven factions argue over engineering doctrine, resource allocation, and command responsibility, not over the need for gate security.
    - Coordinated attacks, unexplained mechanical failures, or evidence that an enemy understands defensive systems are treated as extraordinary dangers.

  - `Deepanvil_City_Profile.md`: Add a **Daily Life and Current Tensions** section reflecting:
    - Deepanvil is not a gate city, but its economy and security are tied to the three major gate cities and to regional cooperation.
    - Daily life emphasizes engineering, mining, maintenance, rescue readiness, clan labor, and practical adaptation to the dead zone.
    - Current tensions focus on food and medicine supply, mining safety, labor demands, clan claims, controlled access to deep excavations, and who receives scarce resonance or Aetherite-related resources.
    - Deepanvil's residents may view gate-city magical dependence skeptically, while gate-city specialists value Deepanvil's dead-zone expertise and nonmagical engineering.

- **Shared current-tension model:**
  - **Accepted system:** Gate defense itself is not normally questioned.
  - **Ordinary disputes:** Costs, permits, contracts, jurisdiction, labor, access, delays, inspections, and unequal benefits.
  - **Professional disputes:** Magical versus technological methods, command structure, redundancy, research limits, and responsibility during emergencies.
  - **Serious warning signs:** Increased incursion frequency, coordinated attackers, intelligent testing, unknown creatures, incorrect ward behavior, compromised procedures, or enemies demonstrating knowledge of the Heart.
  - **Exceptional threat:** Deliberate gate sabotage is not treated as ordinary political rivalry, labor unrest, or commercial competition.

- **Cross-reference and validation work:**
  - Remove implications that all residents are constantly searched, surveilled, or restricted merely for living in a gate city.
  - Concentrate intrusive security at the Heart, gate approaches, transit points, and restricted facilities.
  - Replace casual or routine gate-sabotage hooks with negligence, theft, corruption, unauthorized experiments, falsified records, disguised hostile action, or genuinely apocalyptic intent.
  - Preserve the setting's long-standing human, dwarven, and elven cooperation while allowing cultural competition and political disagreement.
- **Canon decisions required:** None. The Heart-centered security model and normalized gate-city culture were approved during Batch C discussion.
- **Status:** Decision approved.


### Batch C-06 — NPC master-file consolidation and playable profiles

- **Requested outcome:** Rebuild `NPC_Backstory_Personality_file.md` as the canonical NPC identity reference by merging true duplicates, resolving accidental name collisions, separating major officials from routine shop operations, and adding three-line profiles for important leaders and proprietors.
- **Affected files:**
  - `NPC_Backstory_Personality_file.md`
  - `Ravensport_City_Profile.md`
  - `Faerindel_City_Profile.md`
  - `Ironforge_City_Profile.md`
  - `Deepanvil_City_Profile.md`
  - `Captain_Ruriks_Request_Session_0-1.md`
  - `Early_Sessions_Plan_Sessions_0_to_5.md`
  - `Quests_Player_Decisions_Impacts.md`
  - `Enemy_Encounters_Stat_Blocks.md`
  - `DnD_Campaign_World_Bible.md`
  - any other file using a renamed or consolidated NPC
- **Replacement draft:**
  - Use `NPC_Backstory_Personality_file_Batch_C_Working.md` as the approved working replacement text.
- **Identity consolidation:**
  - Remove `Captain Rurik Voss` and consolidate all quest-giver, tavern-owner, sailor, ship, and medallion references under **Captain Elandor "Blackscale" Rurik**.
  - Preserve Harlan Voss only as the retired former Lord Protector and Elara Voss's father.
  - Preserve the approved Ravensport government and military chain from Batch B.
- **Name-collision corrections:**
  - `Lirael "Silverthorn"` → **Maelis "Silverthorn"**
  - `Vesper "the Thread" Crowe` → **Nyra "the Thread" Vell**
  - `Garrick "Ironvein" Deepdelve` → **Brogan Ashdelve**
  - `Thrain Stonehand` → **Dorrin Stonehand**
  - `Garrick Ironclad` → **Torren Ironclad**
  - `Vesper Crowe` → **Corvin Rook**
  - `Harlan Reed` → **Mara Reed**
  - `Lirael Moonveil` → **Caelyra Moonveil**
  - `Vesper Brightsong` → **Saelith Brightsong**
  - `Elandor Leafwhisper` → **Theren Greenbough**
  - `Sylvara Nightbloom` → **Nuala Nightbloom**
  - `Lirael Silverleaf` → **Aelith Silverleaf**
  - `Elowen Thornwhisper` → **Maera Thornwhisper**
  - `Selene Moonwhisper` → **Elira Moonwhisper**
  - Ironforge `Vorn Ironvein` → **Varric Stonecoin**
  - `Lirael Gemheart` → **Runa Gemheart**
  - Deepanvil `Thrain Stonefist` → **Borin Stonefist**
  - `Garrick Deepdelve` → **Korrin Deepdelve**
  - `Helga Ironvein` → **Helga Brassmantle**
  - `Drogath Stoneguard` → **Torag Stoneguard**
  - `Vorn Hammerfall` → **Keldran Hammerfall**
  - `Brannok Gearwright` → **Odrik Gearwright**
- **Leader/proprietor separation:**
  - Lirael Starveil remains Ravensport's Archmage; **Avenna Quillstar** operates the Arcane Emporium.
  - Thalorien Starweaver remains Faerindel's Master Enchanter; **Rhaelor Emberbranch** operates Starforge Atelier under appropriate licenses.
  - Arannis Dawnwhisper remains Lorekeeper; **Ilyan Quillshade** operates the Eternal Quill's public sales and research desk.
  - Saelith Brightsong remains Trade Envoy; **Perrin Brightpath** operates Gateward Traders.
  - Helga Emberforge remains Ironforge's Forge Mistress; **Marta Coalbraid** operates The Anvil's Rest and **Dagna Flintmantle** handles public Great Forge commissions.
  - Brannok Runebeard remains Lorekeeper; **Oskar Deepmug** operates The Deep Hearth and **Odrun Relicward** operates Rune & Relic.
  - Garrick Stonehammer remains Master Engineer; **Berrin Gearlock** operates the associated public engineering workshop.
  - Drogath Stonefist remains Deep Guard commander; **Hargin Shieldthane** manages Deepward Armory.
  - Deepanvil's council leaders no longer personally run taverns or retail counters; dedicated operators are **Brenna Copperkeg**, **Jori Rivetbeard**, **Orsa Blackmantle**, **Renn Quarryhand**, **Pell Tinkerspark**, **Sella Roadcoin**, and **Durn Shieldlock**.
- **Profile standard:**
  - Every important leader and proprietor receives exactly three immediate-run lines: **Appearance**, **Personality + Role**, and **Story Hook**.
  - Early-campaign recurring NPCs may also retain extended motivations, secrets, quirks, and connections.
  - Minor unnamed staff remain generic until they become relevant.
- **Cross-reference and validation work:**
  - Search the repository for every old and new name before implementation.
  - Update city profiles, quest files, sessions, trackers, and encounter references so no retired name remains active.
  - Ensure business ownership, sponsorship, and daily operation are not confused.
  - Replace accidental `Aetherbound` terminology in NPC descriptions with `Veyne's organization` under the Batch B terminology decision.
  - Preserve intentional family relationships only when explicitly documented.
- **Canon decisions required:** None. The user delegated authority to consolidate duplicates, resolve collisions, and complete playable profiles.
- **Status:** Approved working correction set; ready for inclusion in the final Batch C package.


### Batch C-07 — Returned-orb consequence and five open-world fallback quests

- **Requested outcome:** Preserve the possibility that the party persuades Rurik to complete the delivery despite Maelis's warning, and provide five independent quests that can reconnect an uncooperative or highly exploratory party to the campaign's central story.
- **Affected files:**
  - `Captain_Ruriks_Request_Session_0-1.md`
  - `Early_Sessions_Plan_Sessions_0_to_5.md`
  - `Quests_Player_Decisions_Impacts.md`
  - `NPC_Backstory_Personality_file.md`
  - `Enemy_Encounters_Stat_Blocks.md` when encounters are prepared
  - relevant city profiles and geography references
- **Design limitation:** These are quest-ready frameworks, not fixed multi-session scripts. Expand only the quest the players actually pursue.

#### Outcome — Rurik returns the orb despite Maelis's warning

- After Maelis recognizes the unmarked Aetherite power orb and recommends that it remain lost, Rurik initially leans toward refusing Silas.
- The party may still argue that Rurik should honor the contract, avoid provoking Silas, or return the object under controlled conditions.
- Suggested social difficulty:
  - **DC 16 Charisma (Persuasion)** if the party merely argues that the property belongs to the client.
  - **DC 13** if they offer to attend the exchange, protect Rurik, document the handoff, or provide another concrete safeguard.
  - No roll is needed when the DM judges that the party presents overwhelming practical evidence or accepts meaningful responsibility for the consequences.
- On success:
  - Rurik contacts Silas and completes the delivery.
  - The party receives the agreed reward.
  - Maelis does not create a public confrontation, but clearly believes the decision is dangerous.
  - Silas regards the party as competent, potentially useful, and worth observing.
  - Veyne's organization gains another fully charged battery for its established three-crystal transit system, allowing Veyne to prepare or complete another crossing to Aetheron.
  - The party loses immediate access to the orb but does not lose access to the main story.
- Relationship consequences:
  - Rurik remains friendly if the party acted honestly and helped protect his crew.
  - Maelis becomes cautious rather than hostile. She may still warn the party when she learns that Silas or his patron is moving unusually quickly.
  - Silas may later approach the party with paid work, misinformation, or a test of loyalty.
- Campaign consequence:
  - Veyne's schedule advances. Beacon-related operations, unfamiliar technology, or coordinated activity may appear sooner.
  - This is not a campaign failure state. It changes who holds the resource and how quickly the antagonist can act.

## Five Open-World Quest Options

### Quest 1 — The Vanished Supply Caravan

- **Discovery:** A posting at The Caravan Outfitter, a request from Mara Reed or Brogan Ashdelve, or dockside rumors about overdue Deepanvil supplies.
- **Objective:** Locate a missing caravan carrying food, medicine, replacement lift parts, precision tools, and rescue equipment to Deepanvil.
- **Visible stakes:** Deepanvil's poorer districts will face shortages, while delayed medical and rescue supplies may cost lives.
- **Core complication:** The caravan was not attacked for money. False road markers diverted it to a concealed transfer point where selected mechanical components were removed and the survivors were restrained or driven off.
- **Main-story connection:** The stolen components are useful for regulating or constructing a small beacon installation. Shipping marks connect the theft indirectly to buyers associated with Silas.
- **Possible resolutions:** Rescue survivors, recover supplies, track the diverted components, negotiate with hired transport thieves, or expose falsified route records.
- **Reward:** Payment from Deepanvil trade representatives, improved access to dwarven services, and a reliable western contact.
- **Failure consequence:** Deepanvil suffers a temporary supply shortage and Veyne's organization receives the components without interference.

### Quest 2 — The Blue Lantern Auction

- **Discovery:** Corvin Rook offers a rumor, Maelis hears of a private sale, or the party notices invitations marked with a blue lantern symbol.
- **Objective:** Infiltrate or observe a secret Shrouded Wards auction selling restricted magical and dimensional goods.
- **Visible stakes:** Stolen property, dangerous planar specimens, and unregistered magical devices are about to enter private hands.
- **Core complication:** One lot consists of Aetherite shards and a damaged device whose true value is known only to a concealed buyer representing Veyne's organization.
- **Main-story connection:** The buyer's payment records, coded instructions, or courier route identify other Aetherite purchases and western transfers.
- **Possible resolutions:** Pose as buyers, steal the ledger, expose the auction to Thorne Blackwood, bargain with Nyra Vell, replace the target lot, or follow the successful bidder.
- **Reward:** Recovered valuables, criminal intelligence, a favor from city authorities or Nyra, and access to the auction's buyer records.
- **Failure consequence:** The device reaches Veyne's network, but witnesses and payment trails remain available for later investigation.

### Quest 3 — The Third Alarm

- **Discovery:** A public rumor after three unusual Heart alarms, a discreet request from Captain Thorne Blackwood, or a warning passed through Maelis.
- **Objective:** Determine why three separate gate incursions produced nearly identical behavior and timing.
- **Visible stakes:** Routine incursions are expected; coordinated testing of the Heart's defenses is not.
- **Core complication:** Each contained creature carried or had embedded within it the same small manufactured marker. The marker is physical, survives anti-magic screening, and was not created by the creatures themselves.
- **Main-story connection:** The markers record response times, anti-magic activation, and defensive movement, suggesting that an intelligent outside force is testing gate procedures. Their material resembles components used in Aetherite systems without conclusively identifying the maker.
- **Possible resolutions:** Analyze the marker, interview Heart personnel, trace its material through local workshops, inspect where the creatures emerged, or identify someone attempting to purchase defense-response information.
- **Reward:** Official trust, restricted but temporary access to relevant Heart records, and a favor from Ravensport security leadership.
- **Failure consequence:** The testing continues, giving the hostile observer better information about the Heart's defenses.

### Quest 4 — The Silent Orchard

- **Discovery:** A request from Maera Thornwhisper, a Faerindel trade envoy seeking neutral investigators, or merchants reporting that valuable medicinal shipments have stopped.
- **Objective:** Investigate an orchard and medicinal grove where growth, healing magic, and natural magical activity have begun fading in geometric patches.
- **Visible stakes:** The affected plants supply important medicines and restorative compounds throughout the region.
- **Core complication:** The damage is not disease, pollution, or a natural dead-zone expansion. Buried conduits are drawing usable magical energy away from the grove toward an unknown destination.
- **Main-story connection:** The conduits are an early or experimental version of beacon-harvesting technology. Records or construction methods indicate outside funding and mixed elven, dwarven, and human expertise.
- **Possible resolutions:** Remove the conduits, follow them to a collection point, preserve them for study, expose a compromised contractor, or allow controlled operation to identify who returns.
- **Reward:** Medicines, healing assistance, Faerindel goodwill, and access to a knowledgeable magical or botanical specialist.
- **Failure consequence:** The grove's output declines and the hidden collection system continues operating, creating future shortages and a stronger beacon network.

### Quest 5 — The Unclaimed Workshop

- **Discovery:** A landlord reports unpaid rent, Ironforge representatives ask about a missing engineer, or a mechanical accident exposes a sealed basement workshop in Ravensport.
- **Objective:** Determine what happened to the missing craftsperson and secure the machinery left behind.
- **Visible stakes:** The workshop contains dangerous unfinished mechanisms, proprietary dwarven designs, and equipment that could injure nearby residents.
- **Core complication:** The craftsperson was hired to combine reliable anti-magic-compatible machinery with an unfamiliar blue-crystal power interface. They disappeared after realizing the client had concealed the project's true purpose.
- **Main-story connection:** The design is a portable regulator for beacon equipment or an Aetherite-powered weapon platform. Notes refer to a formal intermediary rather than naming Veyne.
- **Possible resolutions:** Find and protect the engineer, dismantle the prototype, complete it as bait, turn it over to Ironforge, sell it, or follow the client's retrieval team.
- **Reward:** Payment, a mechanical prototype or service credit, Ironforge goodwill, and technical evidence connecting conventional engineering to Aetherite infrastructure.
- **Failure consequence:** Veyne's organization recovers the prototype and the missing engineer remains at risk, but the design may reappear later in enemy equipment.

## Open-World Use Rules

- All five quests can exist simultaneously as rumors, postings, private requests, or developing problems.
- Do not force the party toward the orb, Silas, Deepanvil, or a beacon after they refuse those leads.
- Each quest must stand on its own with a clear local reason to care.
- Every quest contains at least one recoverable connection to the central plot, but players may complete it without understanding that connection immediately.
- Failed checks do not erase a quest. They change cost, timing, witnesses, opposition, or which clue survives.
- Failure does not end the campaign. It advances the antagonist, worsens a local problem, or moves evidence elsewhere.
- Prepare encounter statistics only after the party selects a quest and their level, approach, and party composition are known.
- **Canon decisions required:** None. The user approved an open-world structure with five fallback quests and on-demand expansion.
- **Status:** Approved working framework.


### Batch C-08 — Starter combat roster and quest-state tracking

- **Requested outcome:** Complete the remaining starter-arc preparation by adding actionable combat statistics, optional opposition for every prepared quest, an early-Veyne encounter contingency, branch statuses, baseline NPC attitudes, and Veyne-organization interest tracking.
- **Affected files:**
  - `Enemy_Encounters_Stat_Blocks.md`
  - `Quests_Player_Decisions_Impacts.md`
  - `Captain_Ruriks_Request_Session_0-1.md`
  - `Early_Sessions_Plan_Sessions_0_to_5.md`
  - `NPC_Backstory_Personality_file.md`
- **Replacement drafts:**
  - Use `Enemy_Encounters_Stat_Blocks_Batch_C_Working.md` as the working replacement for the encounter file.
  - Use `Quests_Player_Decisions_Impacts_Batch_C_Working.md` as the working replacement for the quest tracker.
- **Encounter additions:**
  - Complete attack bonuses, damage, CR, roles, relevant abilities, tactics, evidence, and dead-zone variants.
  - Retain actionable guard entries for legal complications.
  - Add only starter-relevant opposition: Dockside Lookout, Smuggler, Smuggler Enforcer, Route Thief, Silent Hand Operative, Aetherite Retrieval Specialist, Silas Crowe, Beacon Operator, Workshop Defense Automaton, Aetherite Survey Construct, Conduit Warden, Dead-Zone Stalker, and Marked Gate Beast.
  - Add Lord Cassian Veyne as an explicitly unbalanced early-encounter contingency because open-world player choices may produce an unexpected confrontation.
  - Do not use Veyne as a routine combat encounter. Preserve the possibility that exceptional planning can defeat him and change the campaign.
  - Map possible enemies and noncombat complications to Captain Rurik's Request and all five fallback quests.
- **Quest tracking additions:**
  - Keep Captain Rurik's Request at **Not Started** before play.
  - Add `Potential` and `Locked` branch states with exact unlock conditions.
  - Add all five open-world quests as `Potential`.
  - Add baseline attitudes for Rurik, Maelis, Silas, Nyra, Thorne Blackwood, Lirael Starveil, Brogan Ashdelve, and Veyne.
  - Replace retired `Aetherbound interest` wording with **Veyne's Organization Interest**.
  - Begin interest at level 0 before play and provide a six-state scale from Unaware through Elimination Authorized.
  - Track orb ownership, charges, branch choices, organization interest, and session consequences in one place.
- **Combat philosophy:**
  - Conversations, investigation, stealth, bribery, escape, and surrender remain valid.
  - Ordinary criminals generally avoid dying for cargo.
  - Veyne's trained subordinates attempt to recover evidence and silence witnesses after the party knows too much.
  - Failure advances threats or changes quests rather than ending the campaign.
- **Cross-reference and validation work:**
  - Synchronize `Lirael "Silverthorn"` to **Maelis "Silverthorn"**.
  - Synchronize quest enemies and NPC names with the Batch C NPC master replacement.
  - Add encounter references to the quest and early-session files without forcing fights.
  - Do not add later-campaign enemies until the selected quest, party level, and approach are known.
- **Canon decisions required:** None. The user approved optional combat for every quest, open-world consequences, lethal Veyne operatives when secrecy requires it, and an early BBEG encounter contingency.
- **Status:** Approved working replacement set; completes the currently identified Batch C preparation tasks.

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
