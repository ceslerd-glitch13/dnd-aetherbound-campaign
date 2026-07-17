---
status: Reference
authority: Combat Preparation Guideline
version: 1.0
last_reviewed: 2026-07-16
---

# Guideline: Battle & Stat Block Management

**Purpose**: This document provides a clear process for handling stat blocks and combat encounters. It ensures consistency across the campaign, especially when battles are requested in different conversations or chats.

---

## Core Principle
**Always check the existing repository first.**  
The master file is:  
**`../combat/Enemy_Encounters_Stat_Blocks.md`**

This file contains all custom and campaign-specific stat blocks (guards, NPCs, monsters, etc.).

---

## Step-by-Step Process When a Battle or Stat Block Is Requested

### 1. Check the Existing Repository First
- Open and search `../combat/Enemy_Encounters_Stat_Blocks.md`.
- Look for the requested creature, NPC, or enemy type.
- If it exists → Use or adapt the existing block.

### 2. If the Stat Block Is Missing
Follow this order:

1. **Search the repository thoroughly** (including variants like "hobgoblin captain", "elite guard", etc.).
2. **If still not found**:
   - Look up the official stat block from reliable sources:
     - D&D 5e Monster Manual
     - D&D Beyond (official)
     - Basic Rules / System Reference Document (SRD)
   - Use the **official** version as the baseline.
3. **Create a new entry** in `../combat/Enemy_Encounters_Stat_Blocks.md` using the campaign’s standard format (see below).

### 3. Standard Stat Block Format (Use This Structure)
When adding or creating a new stat block, include at minimum:

- **Name / Type**
- **CR** (Challenge Rating) if known
- **AC** (Armor Class)
- **HP** (Hit Points) with average and/or dice formula
- **Speed**
- **Key Attacks** (weapons + bonuses + damage)
- **Key Abilities / Special Features** (brief)
- **Important Items / Loot** they might carry
- **Possible Loot Table** (especially for random encounters)
- **Notes** (any campaign-specific changes or context)

**Example Structure** (copy this format):
```
**Creature Name**

**CR** X  
**AC** XX  
**HP** XX (XdX + X)  
**Speed** 30 ft.

**Key Attacks**:
- Weapon +X to hit, XdX + X damage

**Important Items**:
- List of notable gear

**Possible Loot**:
- Roll table or options
```

### 4. What to Prioritize When Creating/Using Stat Blocks
Always ensure these are covered:
- **AC** (Armor Class)
- **HP** and how it’s calculated
- **Main attacks** (weapons or special abilities)
- **Key equipment** the creature is using
- **Loot / Treasure** they might drop
- Any **campaign-specific modifications** (e.g., “this hobgoblin has a firearm” or “this guard is level 5 instead of the basic version”)

You do **not** need to copy every single ability from the Monster Manual unless it’s relevant. Focus on what matters for the encounter.

### 5. Handling Homebrew or Modified Creatures
- If the user requests a modified version (e.g., “a hobgoblin with a gun”), create a new entry based on the official block.
- Clearly note what was changed.
- Add it to the repository with a descriptive name (e.g., “Hobgoblin Gunner” or “Elite Gate Warden”).

### 6. Best Practices
- **Consistency first** — reuse existing blocks when possible.
- **Keep the repository organized** (group by type: Guards, Monsters, Bosses, etc.).
- When in doubt, ask the user for clarification on level, modifications, or context.
- For random encounters, always include a **loot table** (even a simple one).
- Remember: Dead zones and technology can affect how creatures fight (e.g., no magic for spellcasters inside dead zones).

### 7. Quick Reference Checklist Before Finalizing Any Stat Block
- [ ] AC is listed
- [ ] HP is listed with average/dice
- [ ] Main attacks are clear
- [ ] Equipment / weapons are noted
- [ ] Loot options are included
- [ ] Any campaign-specific changes are documented
- [ ] The block is added to `../combat/Enemy_Encounters_Stat_Blocks.md`

---

**Final Note**:
This guideline exists so that no matter which chat or conversation a battle request comes from, the process remains the same:
1. Check the repository.
2. Use existing blocks when possible.
3. Look up official sources if missing.
4. Add new blocks in the correct format.

This keeps the campaign consistent and accurate over time.