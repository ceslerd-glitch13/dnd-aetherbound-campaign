---
status: Reference
authority: Creature Catalog Planning and Navigation
version: 1.0
last_reviewed: 2026-07-19
review_state: Reorganized from the supplied 161-creature master package; creature-specific placement and dead-zone adjudication remain subordinate to canon authorities
---

# Elyndria Creature Catalog

## Purpose

This is the repository entry point for official-creature discovery, regional placement planning, gate-incursion preparation, source selection, and dead-zone adjudication notes.

It is an operational **reference**, not a second combat-stat authority and not automatic setting canon. The World Bible controls setting-wide mechanics, Geography controls place names and spatial facts, and `../combat/Enemy_Encounters_Stat_Blocks.md` controls custom campaign statistics.

## Catalog Snapshot

- **Creatures:** 161
- **Category files:** 23
- **Repository groups:** 4
- **Structured data:** `data/creatures.json`
- **Tabular mirror:** `data/creatures.csv`
- **Integrity record:** `manifest.json`
- **Random encounter tables:** [`roll_tables/Roll_Table_Index.md`](roll_tables/Roll_Table_Index.md), containing 23 d6 tables and 138 results

## Find Information Without Opening Every File

- **Random encounter roll:** begin with [`roll_tables/Roll_Table_Index.md`](roll_tables/Roll_Table_Index.md), roll first, and then follow its direct catalog-entry links.
- **Creature name or category:** use the alphabetical table below.
- **Region, habitat, or major city:** use [`lookups/Creature_Regional_Lookup.md`](lookups/Creature_Regional_Lookup.md).
- **CR band or gate-city suitability:** use [`lookups/Creature_Encounter_Lookup.md`](lookups/Creature_Encounter_Lookup.md).
- **Dead-zone dependency, adjudication, or source baseline:** use [`lookups/Creature_Dead_Zone_and_Source_Lookup.md`](lookups/Creature_Dead_Zone_and_Source_Lookup.md).
- **Machine search or filtering:** use `data/creatures.json` or `data/creatures.csv` with [`data/Creature_Data_Schema.md`](data/Creature_Data_Schema.md).

## Authority Boundaries

1. `../canon/DnD_Campaign_World_Bible.md` outranks every creature-specific dead-zone recommendation.
2. `../canon/World_Geography.md` outranks proposed regional wording when a place name or spatial relationship differs.
3. Published creature entries must be opened from an owned official source before live play.
4. `../combat/Enemy_Encounters_Stat_Blocks.md` owns custom or materially altered campaign statistics.
5. A catalog entry identifies a usable option; it does not force that creature to exist in every listed location or appear in play.

## Deferred or Explicitly Unresolved Decisions

- Giant Elk and Giant Owl remain excluded pending a version-specific decision.
- Dryad survival duration, Redcap deterioration, Quickling speed loss, selected spore effects, construct shutdown timing, and elemental collapse timing remain DM adjudications.
- A proposed nonmagical adaptation of an official magical construct requires separate approval.

## Category Directory

| Repository group | Category | Count | File |
|---|---|---:|---|
| Constructs and Animated Objects | Clockwork Construct Adaptation Chassis | 4 | [Open](catalog/constructs_and_animated/Clockwork_Construct_Adaptation_Chassis.md) |
| Constructs and Animated Objects | Magically Animated Constructs and Objects | 11 | [Open](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md) |
| Gate Incursions and Elementals | Major Elemental Gate Creatures | 5 | [Open](catalog/gate_incursions/Major_Elemental_Gate_Creatures.md) |
| Gate Incursions and Elementals | Minor Elemental Gate Creatures | 9 | [Open](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md) |
| Gate Incursions and Elementals | Minor and Moderate Gate Incursions | 10 | [Open](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md) |
| Gate Incursions and Elementals | Severe Gate Incursions | 11 | [Open](catalog/gate_incursions/Severe_Gate_Incursions.md) |
| Natural Ecology and Wildlife | Aerial and Cliff-Dwelling Wildlife | 3 | [Open](catalog/natural_ecology/Aerial_and_Cliff_Dwelling_Wildlife.md) |
| Natural Ecology and Wildlife | Approved Nonmagical Oozes | 4 | [Open](catalog/natural_ecology/Approved_Nonmagical_Oozes.md) |
| Natural Ecology and Wildlife | Aquatic, Wetland and Coastal Wildlife | 9 | [Open](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md) |
| Natural Ecology and Wildlife | Cavern, Mine and Burrowing Predators | 8 | [Open](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md) |
| Natural Ecology and Wildlife | Cold-Region Predators | 7 | [Open](catalog/natural_ecology/Cold_Region_Predators.md) |
| Natural Ecology and Wildlife | Freshwater, Marsh, and Deep-Water Wildlife | 7 | [Open](catalog/natural_ecology/Freshwater_Marsh_and_Deep_Water_Wildlife.md) |
| Natural Ecology and Wildlife | Hoofed Animals and Megafauna | 5 | [Open](catalog/natural_ecology/Hoofed_Animals_and_Megafauna.md) |
| Natural Ecology and Wildlife | Physical Fungi, Myconids, and Predatory Plants | 6 | [Open](catalog/natural_ecology/Physical_Fungi_Myconids_and_Predatory_Plants.md) |
| Natural Ecology and Wildlife | Southern-Plains Wildlife | 9 | [Open](catalog/natural_ecology/Southern_Plains_Wildlife.md) |
| Natural Ecology and Wildlife | Swarms and Small Vermin | 6 | [Open](catalog/natural_ecology/Swarms_and_Small_Vermin.md) |
| Natural Ecology and Wildlife | Venomous Animals and Large Insects | 12 | [Open](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md) |
| Natural Ecology and Wildlife | Wolves and Large Predators | 5 | [Open](catalog/natural_ecology/Wolves_and_Large_Predators.md) |
| Planar, Escaped, and Magical Creatures | Captured and Transported Monstrosities | 6 | [Open](catalog/planar_and_magical/Captured_and_Transported_Monstrosities.md) |
| Planar, Escaped, and Magical Creatures | Fey and Ethereal Predators | 3 | [Open](catalog/planar_and_magical/Fey_and_Ethereal_Predators.md) |
| Planar, Escaped, and Magical Creatures | Fey and Magical Wilderness Creatures | 11 | [Open](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md) |
| Planar, Escaped, and Magical Creatures | Intelligent Aquatic and Magical Water Threats | 3 | [Open](catalog/planar_and_magical/Intelligent_Aquatic_and_Magical_Water_Threats.md) |
| Planar, Escaped, and Magical Creatures | Magically Sustained Plants and Blights | 7 | [Open](catalog/planar_and_magical/Magically_Sustained_Plants_and_Blights.md) |

## Alphabetical Creature Directory

| Creature | CR | Type | Category | Campaign classification |
|---|---:|---|---|---|
| [Abominable Yeti](catalog/natural_ecology/Cold_Region_Predators.md#abominable-yeti) | 9 | Monstrosity | Cold-Region Predators | Natural, exceptional |
| [Adult Kruthik](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#adult-kruthik) | 2 | Monstrosity | Venomous Animals and Large Insects | Planar invasive |
| [Air Elemental](catalog/gate_incursions/Major_Elemental_Gate_Creatures.md#air-elemental) | 5 | Elemental | Major Elemental Gate Creatures | Severe planar elemental |
| [Animated Armor](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#animated-armor) | 1 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Animated Flying Sword](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#animated-flying-sword) | 1/4 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Animated Rug of Smothering](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#animated-rug-of-smothering) | 2 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Ankheg](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md#ankheg) | 2 | Monstrosity | Cavern, Mine and Burrowing Predators | Natural |
| [Assassin Vine](catalog/natural_ecology/Physical_Fungi_Myconids_and_Predatory_Plants.md#assassin-vine) | 3 | Plant | Physical Fungi, Myconids, and Predatory Plants | Rare natural predatory plant or escaped specimen |
| [Awakened Shrub](catalog/planar_and_magical/Magically_Sustained_Plants_and_Blights.md#awakened-shrub) | 0 | Plant | Magically Sustained Plants and Blights | Magically awakened individual |
| [Awakened Tree](catalog/planar_and_magical/Magically_Sustained_Plants_and_Blights.md#awakened-tree) | 2 | Plant | Magically Sustained Plants and Blights | Magically awakened individual |
| [Axe Beak](catalog/natural_ecology/Southern_Plains_Wildlife.md#axe-beak) | 1/4 | Beast | Southern-Plains Wildlife | Natural |
| [Azer](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#azer) | 2 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Barlgura](catalog/gate_incursions/Severe_Gate_Incursions.md#barlgura) | 5 | Fiend (Demon) | Severe Gate Incursions | Planar |
| [Basilisk](catalog/planar_and_magical/Captured_and_Transported_Monstrosities.md#basilisk) | 3 | Monstrosity | Captured and Transported Monstrosities | Planar or escaped |
| [Black Bear](catalog/natural_ecology/Wolves_and_Large_Predators.md#black-bear) | 1/2 | Beast | Wolves and Large Predators | Natural |
| [Black Pudding](catalog/natural_ecology/Approved_Nonmagical_Oozes.md#black-pudding) | 4 | Ooze | Approved Nonmagical Oozes | Approved unintelligent nonmagical organism |
| [Blink Dog](catalog/planar_and_magical/Fey_and_Ethereal_Predators.md#blink-dog) | 1/4 | Fey | Fey and Ethereal Predators | Planar or escaped |
| [Blue Slaad](catalog/gate_incursions/Severe_Gate_Incursions.md#blue-slaad) | 7 | Aberration | Severe Gate Incursions | Planar |
| [Boar](catalog/natural_ecology/Hoofed_Animals_and_Megafauna.md#boar) | 1/4 | Beast | Hoofed Animals and Megafauna | Natural |
| [Boggle](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#boggle) | 1/8 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Bone Devil](catalog/gate_incursions/Severe_Gate_Incursions.md#bone-devil) | 9 | Fiend (Devil) | Severe Gate Incursions | Planar |
| [Bronze Scout](catalog/constructs_and_animated/Clockwork_Construct_Adaptation_Chassis.md#bronze-scout) | 1 | Construct | Clockwork Construct Adaptation Chassis | Official magical construct and possible chassis for a separate nonmagical Elyndrian variant |
| [Brown Bear](catalog/natural_ecology/Wolves_and_Large_Predators.md#brown-bear) | 1 | Beast | Wolves and Large Predators | Natural |
| [Bulette](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md#bulette) | 5 | Monstrosity | Cavern, Mine and Burrowing Predators | Natural |
| [Carrion Crawler](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md#carrion-crawler) | 2 | Monstrosity | Cavern, Mine and Burrowing Predators | Natural |
| [Cave Fisher](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md#cave-fisher) | 3 | Monstrosity | Cavern, Mine and Burrowing Predators | Natural cavern predator |
| [Chain Devil](catalog/gate_incursions/Severe_Gate_Incursions.md#chain-devil) | 8 | Fiend (Devil) | Severe Gate Incursions | Planar |
| [Chasme](catalog/gate_incursions/Severe_Gate_Incursions.md#chasme) | 6 | Fiend (Demon) | Severe Gate Incursions | Planar |
| [Chuul](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#chuul) | 4 | Aberration | Minor and Moderate Gate Incursions | Planar or escaped |
| [Clay Golem](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#clay-golem) | 9 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Cockatrice](catalog/planar_and_magical/Captured_and_Transported_Monstrosities.md#cockatrice) | 1/2 | Monstrosity | Captured and Transported Monstrosities | Planar or escaped |
| [Crocodile](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#crocodile) | 1/2 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Darkling](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#darkling) | 1/2 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Darkmantle](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md#darkmantle) | 1/2 | Monstrosity | Cavern, Mine and Burrowing Predators | Natural cavern predator |
| [Death Dog](catalog/planar_and_magical/Captured_and_Transported_Monstrosities.md#death-dog) | 1 | Monstrosity | Captured and Transported Monstrosities | Planar or escaped |
| [Dire Wolf](catalog/natural_ecology/Wolves_and_Large_Predators.md#dire-wolf) | 1 | Beast | Wolves and Large Predators | Natural |
| [Displacer Beast](catalog/planar_and_magical/Fey_and_Ethereal_Predators.md#displacer-beast) | 3 | Monstrosity | Fey and Ethereal Predators | Planar or escaped |
| [Dretch](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#dretch) | 1/4 | Fiend (Demon) | Minor and Moderate Gate Incursions | Planar |
| [Dryad](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#dryad) | 1 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Dust Mephit](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#dust-mephit) | 1/2 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Earth Elemental](catalog/gate_incursions/Major_Elemental_Gate_Creatures.md#earth-elemental) | 5 | Elemental | Major Elemental Gate Creatures | Severe planar elemental |
| [Elephant](catalog/natural_ecology/Southern_Plains_Wildlife.md#elephant) | 4 | Beast | Southern-Plains Wildlife | Natural |
| [Elk](catalog/natural_ecology/Hoofed_Animals_and_Megafauna.md#elk) | 1/4 | Beast | Hoofed Animals and Megafauna | Natural |
| [Fire Elemental](catalog/gate_incursions/Major_Elemental_Gate_Creatures.md#fire-elemental) | 5 | Elemental | Major Elemental Gate Creatures | Severe planar elemental |
| [Fire Snake](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#fire-snake) | 1 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Flesh Golem](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#flesh-golem) | 5 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Frost Salamander](catalog/natural_ecology/Cold_Region_Predators.md#frost-salamander) | 9 | Elemental | Cold-Region Predators | Planar or escaped |
| [Galeb Duhr](catalog/gate_incursions/Major_Elemental_Gate_Creatures.md#galeb-duhr) | 6 | Elemental | Major Elemental Gate Creatures | Planar elemental guardian |
| [Gargoyle](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#gargoyle) | 2 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Gas Spore Fungus](catalog/natural_ecology/Physical_Fungi_Myconids_and_Predatory_Plants.md#gas-spore-fungus) | 1/2 | Plant | Physical Fungi, Myconids, and Predatory Plants | Rare natural organism, invasive, or escaped specimen |
| [Gelatinous Cube](catalog/natural_ecology/Approved_Nonmagical_Oozes.md#gelatinous-cube) | 2 | Ooze | Approved Nonmagical Oozes | Approved unintelligent nonmagical organism |
| [Giant Bat](catalog/natural_ecology/Aerial_and_Cliff_Dwelling_Wildlife.md#giant-bat) | 1/4 | Beast | Aerial and Cliff-Dwelling Wildlife | Natural |
| [Giant Boar](catalog/natural_ecology/Hoofed_Animals_and_Megafauna.md#giant-boar) | 2 | Beast | Hoofed Animals and Megafauna | Natural |
| [Giant Centipede](catalog/natural_ecology/Swarms_and_Small_Vermin.md#giant-centipede) | 1/4 | Beast | Swarms and Small Vermin | Natural |
| [Giant Constrictor Snake](catalog/natural_ecology/Freshwater_Marsh_and_Deep_Water_Wildlife.md#giant-constrictor-snake) | 2 | Beast | Freshwater, Marsh, and Deep-Water Wildlife | Natural |
| [Giant Crab](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#giant-crab) | 1/8 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Giant Crocodile](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#giant-crocodile) | 5 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Giant Dragonfly](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#giant-dragonfly) | 1/2 | Beast | Venomous Animals and Large Insects | Natural |
| [Giant Fire Beetle](catalog/natural_ecology/Swarms_and_Small_Vermin.md#giant-fire-beetle) | 0 | Beast | Swarms and Small Vermin | Natural |
| [Giant Frog](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#giant-frog) | 1/4 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Giant Goat](catalog/natural_ecology/Hoofed_Animals_and_Megafauna.md#giant-goat) | 1/2 | Beast | Hoofed Animals and Megafauna | Natural |
| [Giant Hyena](catalog/natural_ecology/Southern_Plains_Wildlife.md#giant-hyena) | 1 | Beast | Southern-Plains Wildlife | Natural |
| [Giant Lizard](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md#giant-lizard) | 1/4 | Beast | Cavern, Mine and Burrowing Predators | Natural |
| [Giant Octopus](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#giant-octopus) | 1 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Giant Scorpion](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#giant-scorpion) | 3 | Beast | Venomous Animals and Large Insects | Natural |
| [Giant Sea Eel](catalog/natural_ecology/Freshwater_Marsh_and_Deep_Water_Wildlife.md#giant-sea-eel) | 1/2 | Beast | Freshwater, Marsh, and Deep-Water Wildlife | Natural |
| [Giant Shark](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#giant-shark) | 5 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Giant Snapping Turtle](catalog/natural_ecology/Freshwater_Marsh_and_Deep_Water_Wildlife.md#giant-snapping-turtle) | 3 | Beast | Freshwater, Marsh, and Deep-Water Wildlife | Natural |
| [Giant Spider](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md#giant-spider) | 1 | Beast | Cavern, Mine and Burrowing Predators | Natural |
| [Giant Squid](catalog/natural_ecology/Freshwater_Marsh_and_Deep_Water_Wildlife.md#giant-squid) | 6 | Beast | Freshwater, Marsh, and Deep-Water Wildlife | Natural, exceptionally rare |
| [Giant Toad](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#giant-toad) | 1 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Giant Venomous Snake](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#giant-venomous-snake) | 1/4 | Beast | Venomous Animals and Large Insects | Natural |
| [Giant Vulture](catalog/natural_ecology/Southern_Plains_Wildlife.md#giant-vulture) | 1 | Beast | Southern-Plains Wildlife | Natural |
| [Giant Wasp](catalog/natural_ecology/Aerial_and_Cliff_Dwelling_Wildlife.md#giant-wasp) | 1/2 | Beast | Aerial and Cliff-Dwelling Wildlife | Natural |
| [Giant Wolf Spider](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#giant-wolf-spider) | 1/4 | Beast | Venomous Animals and Large Insects | Natural |
| [Gibbering Mouther](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#gibbering-mouther) | 2 | Aberration | Minor and Moderate Gate Incursions | Planar or escaped |
| [Gray Ooze](catalog/natural_ecology/Approved_Nonmagical_Oozes.md#gray-ooze) | 1/2 | Ooze | Approved Nonmagical Oozes | Approved unintelligent nonmagical organism |
| [Green Hag](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#green-hag) | 3 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Green Slaad](catalog/gate_incursions/Severe_Gate_Incursions.md#green-slaad) | 8 | Aberration (Shapechanger) | Severe Gate Incursions | Planar |
| [Hell Hound](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#hell-hound) | 3 | Fiend | Minor and Moderate Gate Incursions | Planar or escaped |
| [Helmed Horror](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#helmed-horror) | 4 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Hezrou](catalog/gate_incursions/Severe_Gate_Incursions.md#hezrou) | 8 | Fiend (Demon) | Severe Gate Incursions | Planar |
| [Homunculus](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#homunculus) | 0 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Hunter Shark](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#hunter-shark) | 2 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Hyena](catalog/natural_ecology/Southern_Plains_Wildlife.md#hyena) | 0 | Beast | Southern-Plains Wildlife | Natural |
| [Ice Mephit](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#ice-mephit) | 1/2 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Imp](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#imp) | 1 | Fiend (Devil) | Minor and Moderate Gate Incursions | Planar |
| [Invisible Stalker](catalog/gate_incursions/Severe_Gate_Incursions.md#invisible-stalker) | 6 | Elemental | Severe Gate Incursions | Planar |
| [Iron Cobra](catalog/constructs_and_animated/Clockwork_Construct_Adaptation_Chassis.md#iron-cobra) | 4 | Construct | Clockwork Construct Adaptation Chassis | Official magical construct and possible chassis for a separate nonmagical Elyndrian variant |
| [Iron Golem](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#iron-golem) | 16 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Killer Whale](catalog/natural_ecology/Freshwater_Marsh_and_Deep_Water_Wildlife.md#killer-whale) | 3 | Beast | Freshwater, Marsh, and Deep-Water Wildlife | Natural |
| [Kruthik Hive Lord](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#kruthik-hive-lord) | 5 | Monstrosity | Venomous Animals and Large Insects | Planar invasive |
| [Lion](catalog/natural_ecology/Southern_Plains_Wildlife.md#lion) | 1 | Beast | Southern-Plains Wildlife | Natural |
| [Magma Mephit](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#magma-mephit) | 1/2 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Magmin](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#magmin) | 1/2 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Mammoth](catalog/natural_ecology/Hoofed_Animals_and_Megafauna.md#mammoth) | 6 | Beast | Hoofed Animals and Megafauna | Natural |
| [Manticore](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#manticore) | 3 | Monstrosity | Minor and Moderate Gate Incursions | Planar |
| [Meenlock](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#meenlock) | 2 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Merrow](catalog/planar_and_magical/Intelligent_Aquatic_and_Magical_Water_Threats.md#merrow) | 2 | Monstrosity | Intelligent Aquatic and Magical Water Threats | Planar or gate-established raider |
| [Mimic](catalog/planar_and_magical/Captured_and_Transported_Monstrosities.md#mimic) | 2 | Monstrosity | Captured and Transported Monstrosities | Escaped specimen |
| [Mud Mephit](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#mud-mephit) | 1/4 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Myconid Adult](catalog/natural_ecology/Physical_Fungi_Myconids_and_Predatory_Plants.md#myconid-adult) | 1/2 | Plant | Physical Fungi, Myconids, and Predatory Plants | Sentient fungal person |
| [Myconid Sprout](catalog/natural_ecology/Physical_Fungi_Myconids_and_Predatory_Plants.md#myconid-sprout) | 0 | Plant | Physical Fungi, Myconids, and Predatory Plants | Sentient fungal person |
| [Needle Blight](catalog/planar_and_magical/Magically_Sustained_Plants_and_Blights.md#needle-blight) | 1/4 | Plant | Magically Sustained Plants and Blights | Magically animated hostile plant |
| [Oaken Bolter](catalog/constructs_and_animated/Clockwork_Construct_Adaptation_Chassis.md#oaken-bolter) | 5 | Construct | Clockwork Construct Adaptation Chassis | Official magical construct and possible chassis for a separate nonmagical Elyndrian variant |
| [Ochre Jelly](catalog/natural_ecology/Approved_Nonmagical_Oozes.md#ochre-jelly) | 2 | Ooze | Approved Nonmagical Oozes | Approved unintelligent nonmagical organism |
| [Panther](catalog/natural_ecology/Southern_Plains_Wildlife.md#panther) | 1/4 | Beast | Southern-Plains Wildlife | Natural |
| [Phase Spider](catalog/planar_and_magical/Fey_and_Ethereal_Predators.md#phase-spider) | 3 | Monstrosity | Fey and Ethereal Predators | Planar or escaped |
| [Piercer](catalog/natural_ecology/Cavern_Mine_and_Burrowing_Predators.md#piercer) | 1/2 | Monstrosity | Cavern, Mine and Burrowing Predators | Natural cavern predator |
| [Pixie](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#pixie) | 1/4 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Plesiosaurus](catalog/natural_ecology/Freshwater_Marsh_and_Deep_Water_Wildlife.md#plesiosaurus) | 2 | Beast (Dinosaur) | Freshwater, Marsh, and Deep-Water Wildlife | Natural, marine only |
| [Polar Bear](catalog/natural_ecology/Wolves_and_Large_Predators.md#polar-bear) | 2 | Beast | Wolves and Large Predators | Natural |
| [Pteranodon](catalog/natural_ecology/Aerial_and_Cliff_Dwelling_Wildlife.md#pteranodon) | 1/4 | Beast | Aerial and Cliff-Dwelling Wildlife | Natural |
| [Purple Worm](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#purple-worm) | 15 | Monstrosity | Venomous Animals and Large Insects | Exceptional natural apex predator |
| [Quasit](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#quasit) | 1 | Fiend (Demon) | Minor and Moderate Gate Incursions | Planar |
| [Quickling](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#quickling) | 1 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Red Slaad](catalog/gate_incursions/Severe_Gate_Incursions.md#red-slaad) | 5 | Aberration | Severe Gate Incursions | Planar |
| [Redcap](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#redcap) | 3 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Reef Shark](catalog/natural_ecology/Aquatic_Wetland_and_Coastal_Wildlife.md#reef-shark) | 1/2 | Beast | Aquatic, Wetland and Coastal Wildlife | Natural |
| [Remorhaz](catalog/natural_ecology/Cold_Region_Predators.md#remorhaz) | 11 | Monstrosity | Cold-Region Predators | Natural apex predator |
| [Rhinoceros](catalog/natural_ecology/Southern_Plains_Wildlife.md#rhinoceros) | 2 | Beast | Southern-Plains Wildlife | Natural |
| [Roper](catalog/planar_and_magical/Captured_and_Transported_Monstrosities.md#roper) | 5 | Monstrosity | Captured and Transported Monstrosities | Planar, escaped, or established cavern species |
| [Rust Monster](catalog/planar_and_magical/Captured_and_Transported_Monstrosities.md#rust-monster) | 1/2 | Monstrosity | Captured and Transported Monstrosities | Escaped |
| [Saber-Toothed Tiger](catalog/natural_ecology/Cold_Region_Predators.md#saber-toothed-tiger) | 2 | Beast | Cold-Region Predators | Natural |
| [Salamander](catalog/gate_incursions/Severe_Gate_Incursions.md#salamander) | 5 | Elemental | Severe Gate Incursions | Planar |
| [Satyr](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#satyr) | 1/2 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Scarecrow](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#scarecrow) | 1 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Scorpion](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#scorpion) | 0 | Beast | Venomous Animals and Large Insects | Natural |
| [Sea Hag](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#sea-hag) | 2 | Fey | Minor and Moderate Gate Incursions | Planar |
| [Sea Spawn](catalog/planar_and_magical/Intelligent_Aquatic_and_Magical_Water_Threats.md#sea-spawn) | 1 | Humanoid or Monstrosity | Intelligent Aquatic and Magical Water Threats | Altered person or planar servant |
| [Shambling Mound](catalog/planar_and_magical/Magically_Sustained_Plants_and_Blights.md#shambling-mound) | 5 | Plant | Magically Sustained Plants and Blights | Magically sustained plant creature |
| [Shield Guardian](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#shield-guardian) | 7 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Shrieker Fungus](catalog/natural_ecology/Physical_Fungi_Myconids_and_Predatory_Plants.md#shrieker-fungus) | 0 | Plant | Physical Fungi, Myconids, and Predatory Plants | Natural fungus |
| [Smoke Mephit](catalog/gate_incursions/Minor_Elemental_Gate_Creatures.md#smoke-mephit) | 1/4 | Elemental | Minor Elemental Gate Creatures | Planar elemental gate creature |
| [Sprite](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#sprite) | 1/4 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Steam Mephit](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#steam-mephit) | 1/4 | Elemental | Minor and Moderate Gate Incursions | Planar |
| [Stone Defender](catalog/constructs_and_animated/Clockwork_Construct_Adaptation_Chassis.md#stone-defender) | 4 | Construct | Clockwork Construct Adaptation Chassis | Official magical construct and possible chassis for a separate nonmagical Elyndrian variant |
| [Stone Golem](catalog/constructs_and_animated/Magically_Animated_Constructs_and_Objects.md#stone-golem) | 10 | Construct | Magically Animated Constructs and Objects | Magically animated construct |
| [Swarm of Bats](catalog/natural_ecology/Swarms_and_Small_Vermin.md#swarm-of-bats) | 1/4 | Swarm of Tiny Beasts | Swarms and Small Vermin | Natural |
| [Swarm of Insects](catalog/natural_ecology/Swarms_and_Small_Vermin.md#swarm-of-insects) | 1/2 | Swarm of Tiny Beasts | Swarms and Small Vermin | Natural |
| [Swarm of Quippers](catalog/natural_ecology/Freshwater_Marsh_and_Deep_Water_Wildlife.md#swarm-of-quippers) | 1 | Swarm of Tiny Beasts | Freshwater, Marsh, and Deep-Water Wildlife | Natural, localized |
| [Swarm of Rats](catalog/natural_ecology/Swarms_and_Small_Vermin.md#swarm-of-rats) | 1/4 | Swarm of Tiny Beasts | Swarms and Small Vermin | Natural |
| [Swarm of Ravens](catalog/natural_ecology/Swarms_and_Small_Vermin.md#swarm-of-ravens) | 1/4 | Swarm of Tiny Beasts | Swarms and Small Vermin | Natural |
| [Swarm of Venomous Snakes](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#swarm-of-venomous-snakes) | 2 | Swarm of Tiny Beasts | Venomous Animals and Large Insects | Natural |
| [Tiger](catalog/natural_ecology/Southern_Plains_Wildlife.md#tiger) | 1 | Beast | Southern-Plains Wildlife | Natural |
| [Twig Blight](catalog/planar_and_magical/Magically_Sustained_Plants_and_Blights.md#twig-blight) | 1/8 | Plant | Magically Sustained Plants and Blights | Magically animated hostile plant |
| [Umber Hulk](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#umber-hulk) | 5 | Monstrosity | Venomous Animals and Large Insects | Rare subterranean threat |
| [Venomous Snake](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#venomous-snake) | 1/8 | Beast | Venomous Animals and Large Insects | Natural |
| [Vine Blight](catalog/planar_and_magical/Magically_Sustained_Plants_and_Blights.md#vine-blight) | 1/2 | Plant | Magically Sustained Plants and Blights | Magically animated hostile plant |
| [Violet Fungus](catalog/natural_ecology/Physical_Fungi_Myconids_and_Predatory_Plants.md#violet-fungus) | 1/4 | Plant | Physical Fungi, Myconids, and Predatory Plants | Natural fungal predator |
| [Vrock](catalog/gate_incursions/Severe_Gate_Incursions.md#vrock) | 6 | Fiend (Demon) | Severe Gate Incursions | Planar |
| [Water Elemental](catalog/gate_incursions/Major_Elemental_Gate_Creatures.md#water-elemental) | 5 | Elemental | Major Elemental Gate Creatures | Severe planar elemental |
| [Water Weird](catalog/planar_and_magical/Intelligent_Aquatic_and_Magical_Water_Threats.md#water-weird) | 3 | Elemental | Intelligent Aquatic and Magical Water Threats | Planar, summoned, or contained |
| [Winter Wolf](catalog/natural_ecology/Cold_Region_Predators.md#winter-wolf) | 3 | Monstrosity | Cold-Region Predators | Planar or old gate-established |
| [Wolf](catalog/natural_ecology/Wolves_and_Large_Predators.md#wolf) | 1/4 | Beast | Wolves and Large Predators | Natural |
| [Wood Woad](catalog/planar_and_magical/Magically_Sustained_Plants_and_Blights.md#wood-woad) | 5 | Plant | Magically Sustained Plants and Blights | Magically created plant guardian |
| [Xorn](catalog/gate_incursions/Minor_and_Moderate_Gate_Incursions.md#xorn) | 5 | Elemental | Minor and Moderate Gate Incursions | Planar or escaped |
| [Yeth Hound](catalog/planar_and_magical/Fey_and_Magical_Wilderness_Creatures.md#yeth-hound) | 4 | Fey | Fey and Magical Wilderness Creatures | Planar visitor, resident, or escaped fey |
| [Yeti](catalog/natural_ecology/Cold_Region_Predators.md#yeti) | 3 | Monstrosity | Cold-Region Predators | Rare natural magical species |
| [Young Kruthik](catalog/natural_ecology/Venomous_Animals_and_Large_Insects.md#young-kruthik) | 1/8 | Monstrosity | Venomous Animals and Large Insects | Planar invasive |
| [Young Remorhaz](catalog/natural_ecology/Cold_Region_Predators.md#young-remorhaz) | 5 | Monstrosity | Cold-Region Predators | Natural, very rare |
