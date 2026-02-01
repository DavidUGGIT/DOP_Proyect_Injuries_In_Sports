# 🔄 RAW vs PROCESSED - Quick Guide

## Main Differences

### 📊 NBA_Raw (22 columns)
```
Name - Season: "Derrick Rose summary before"
Field goals made-attempted per game: "8,7-18,7"    ← STRING! ❌
Three-point field goals made-attempted: "0,9-2,9"  ← STRING! ❌
Free throws made-attempted: "4,6-5,2"              ← STRING! ❌
GS: 159
games played: 159
```

**Problem:** You can't use this data directly in analysis!

---

### ✨ NBA_Processed (33 columns = 22 + 11 new)
```
Player_Name: "Derrick Rose"           ← NEW! ⭐
Period: "Summary Before"              ← NEW! ⭐
League: "NBA"                         ← NEW! ⭐
Injury_Type: "ACL"                    ← NEW! ⭐

FG_made: 8.7                          ← NEW! Number ✅
FG_attempted: 18.7                    ← NEW! Number ✅
3PT_made: 0.9                         ← NEW! Number ✅
3PT_attempted: 2.9                    ← NEW! Number ✅
FT_made: 4.6                          ← NEW! Number ✅
FT_attempted: 5.2                     ← NEW! Number ✅

GS_percent: 100.0                     ← NEW! Calculated ✅
```

**Advantage:** Everything is ready for analysis! Use this data!

---

##  Usage Example

### ❌ Wrong (with Raw):
```python
# You have to parse strings yourself
df_raw = pd.read_excel(FILE, sheet_name='NBA_Raw')
fg_string = df_raw.iloc[0]['Field goals made-attempted per game']  # "8,7-18,7"
# Now you need to:
# 1. Split by "-"
# 2. Replace "," with "."
# 3. Convert to float
# 4. Calculate FG%
# = 10+ lines of code! 😰
```

### ✅ Correct (with Processed):
```python
# Everything is ready!
df = pd.read_excel(FILE, sheet_name='NBA_Processed')

# One line:
avg_fg_pct = df['FG%'].mean()

# Or:
avg_pts_before = df[df['Period'] == 'Summary Before']['PTS'].mean()

# Or filter by player:
derrick = df[df['Player_Name'] == 'Derrick Rose']
```

---

## Full List of New Columns (Processed)

| Column | Description | Use |
|--------|-------------|-----|
| `Player_Name` | Clean player name | Filter by player |
| `Period` | "Summary Before" / "Summary After" / "Specific Season" | Easy before/after comparisons |
| `League` | "NBA" / "WNBA" | NBA vs WNBA comparisons |
| `Injury_Type` | "ACL" | Injury categorization |
| `FG_made` | Number (float) | Field goals made |
| `FG_attempted` | Number (float) | Field goal attempts |
| `3PT_made` | Number (float) | Three-pointers made |
| `3PT_attempted` | Number (float) | Three-point attempts |
| `FT_made` | Number (float) | Free throws made |
| `FT_attempted` | Number (float) | Free throw attempts |
| `GS_percent` | Percentage (0-100) | % of games started |

---

##  Which sheets to use?

### For ANALYSIS (USE THESE! ⭐):
- ✅ `NBA_Processed`
- ✅ `WNBA_Processed`
- ✅ `Basketball_Combined` (NBA + WNBA together)
- ✅ `Soccer_Processed`
- ✅ `Collegiate_Processed`
- ✅ `Summary_Basketball`
- ✅ `Summary_Soccer`
- ✅ `Summary_Collegiate`

### For ARCHIVE (only if you need the originals):
- 📁 `NBA_Raw`
- 📁 `WNBA_Raw`
- 📁 `Soccer_Raw`
- 📁 `Collegiate_Raw`

---

## 💡 When to use Raw?

**Almost never!** 

Raw is only an archive of the original data. Use it only when:
- You want to check original values
- Something went wrong during processing (very unlikely)
- You want to do DIFFERENT transformations than the ones already done

---
