---
status: Historical
authority: Approved Change Archive
version: 1.0
last_reviewed: 2026-07-17
implementation_status: Applied in validated package; post-upload GitHub verification pending
---

# Pending Changes Archived 06 — Batches E, F, and G

## Archive Status

The user approved the DM scene-anchor work, the minimal reserved shop/item file, and the repository folder organization. This archive records the combined local implementation prepared against GitHub `main` commit `0fa6e2395ae97c0487a1b7a812ffca2cbf8d6d64` on 2026-07-17.

The package is not a GitHub update until the user uploads it and a new commit is visible. After upload, verify the committed tree and GitHub Actions result before changing `implementation_status` to fully verified.

## Implementation Result

1. **Batch E — DM Scene and Location Anchors:** Added working names, relative placement, visible features, information sources, and quest functions for the starter investigation, five open-world quests, and supporting city hooks.
2. **Batch F — Reserved Shop and Item Inventory:** Added a minimal `items/Shop_Inventory_and_Items.md` authority file without inventing inventories or prices.
3. **Batch G — Repository Folder Organization:** Moved campaign content into `canon/`, `cities/`, `npcs/`, `quests/`, `combat/`, `items/`, `guidelines/`, `history/`, and `assets/maps/`; updated references, validator paths, manifest path, and repository navigation.

## Approved New Scene Anchors

- Ravensport: The Wayward Gull, Netmaker's Bunkhouse, Old Gull Sailworks, The Lantern House, Harbor Watchhouse, West Response Annex, three named Heart incident sites, Customs Warehouse Seven, Red Wheel Freight Yard, and Deepanvil Freight Office.
- Western route: Three-Cairn Fork, Split-Wheel Ravine, and The Cold Kiln.
- Faerindel: Stillbloom Orchard, The Rain House, Whitebark Hollow, South Quarantine Glasshouse, and Warden Muster Hall.
- Ironforge: Copperglass Workshop, Ash Rail Spur, Foundry Receiving Hall Three, Emberforge Pattern Vault, and Deep Guard Drill Gallery.
- Deepanvil: Shaft Twelve — Lower Survey Gate, Brassmantle Test Hall, Old Vent Seven, and Gearwright Below-Lab.

## Approved Utility NPCs

- Brask Morrow — Lantern House doorman.
- Iven Pell — Lantern House tally clerk.
- Nollin Brasswire — missing independent engineer.
- Hesta Rivetcloak — Copperglass landlord.

## Structural Rules Preserved

- Root operating files remain visible.
- Canon and authority ownership are unchanged.
- Exact coordinates, floorplans, travel times, and encounter maps remain deliberately undefined.
- The canonical city count, three gate cities, four Ravensport piers, known/hidden dead-zone model, map image bytes, quest states, orb state, antagonist interest, and combat statistics were not changed by the migration.
- The shop/item file remains intentionally minimal pending separate reviewed content.

## Validation and Handoff

The prepared working tree must pass:

```bash
python scripts/validate_repository.py --strict-warnings
```

After upload, verify the new GitHub commit, moved paths, archive, empty active Pending file, Campaign Index, and GitHub Actions result.
