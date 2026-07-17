---
status: Historical
authority: Approved Shop Inventory Change Archive
version: 1.0
last_reviewed: 2026-07-17
implementation_status: Applied in validated local package; post-upload GitHub verification pending
---

# Pending Changes Archived 07 — Batch H Shop and Equipment Integration

## Archive Status

The user supplied the completed shop-recommendation package and approved its review and integration into the organized repository package. This archive records the approved local implementation prepared against GitHub `main` commit `0fa6e2395ae97c0487a1b7a812ffca2cbf8d6d64`.

Nothing is a GitHub update until the user uploads the package and a new commit is verified.

## Implemented Scope

- Replaced the minimal Draft `items/Shop_Inventory_and_Items.md` placeholder with a complete Reference authority.
- Added inventories and purchasing guidance for all 24 named commercial locations in Ravensport, Deepanvil, Faerindel, and Ironforge.
- Added useful sale guidance for all eight named inns and taverns.
- Added distinct black-market availability and consequences for all four profiled cities.
- Added equipment templates and availability assignments for all 35 canonical cities plus Westlake Port.
- Added medical, herbalist, apothecary, alchemical, firearm, poison, explosive, vehicle, Aetherite, and dead-zone guidance.
- Added short cross-references to all four city profiles without duplicating their full inventory lists.
- Updated the Campaign Index and active Pending metadata.

## Approved Decisions

1. The approved equipment-price baseline is the D&D Beyond equipment snapshot reviewed on 2026-07-17, with clearly marked 2014 legacy gaps retained where useful to the campaign.
2. Ordinary pistols and muskets exist as licensed specialist goods.
3. Modern, automatic, energy, and antimatter weapons are not normal commerce and remain restricted dimensional finds or story-only equipment.
4. Airships remain story-only rather than ordinary Elyndrian transport.
5. Deepanvil and Ironforge retain unnamed city-level medical and alchemical services; no new proprietor or storefront was created.
6. Black-market lists represent possible access, not guaranteed stock. Serious purchases require appropriate contacts and consequences.
7. Aetherite, resonance, Gate Heart, and Aetheronian technology has no automatic retail price.

## Review Adjustments

- Used the already-approved `items/Shop_Inventory_and_Items.md` authority instead of creating a competing `Elyndria_Shop_Inventory_Reference.md` file.
- Kept the repository audit and approval-plan source documents outside active canon; only their reviewed operational content was integrated.
- Changed the broad explosive wording so bombs are possible contraband based on city and contact rather than guaranteed common stock in every black market.
- Frozen external prices to the dated campaign snapshot so future website changes do not silently alter campaign economics.

## Validation Requirement

The prepared repository must pass:

```bash
python scripts/validate_repository.py --strict-warnings
```

After upload, verify the committed paths, item authority, city cross-references, archive, empty active Pending file, Campaign Index, and GitHub Actions result.
