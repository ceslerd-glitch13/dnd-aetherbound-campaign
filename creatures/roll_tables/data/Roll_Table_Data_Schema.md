
# Creature Roll Table Data Schema

`roll_tables.json` is the synchronized structured record. `roll_tables.csv` is its spreadsheet-friendly mirror.

## Result fields

| Field | Meaning |
|---|---|
| `table_number` | Stable supplied table number, 1 through 23 |
| `table_title` | Human-readable table title |
| `roll_table_group` | Repository group containing the table |
| `table_file` | Path relative to `creatures/roll_tables/` |
| `roll` | d6 result, 1 through 6 |
| `encounter_group` | Original encounter-group wording |
| `total_creatures` | Total creatures in the result |
| `gate_invasion` | Whether the result is a campaign-scale gate force |
| `catalog_entries` | Creature components that must be consulted after the roll |

## Catalog-entry fields

| Field | Meaning |
|---|---|
| `count` | Number of this creature in the result |
| `display_name` | Pluralized or displayed source wording |
| `name` | Canonical creature-catalog name |
| `catalog_file` | Creature category file relative to `creatures/` |
| `entry_anchor` | Direct Markdown anchor for the creature entry |

Every result must resolve entirely to creature records in `../../data/creatures.json`.
