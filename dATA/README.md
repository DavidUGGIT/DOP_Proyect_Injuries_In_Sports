# 🏀⚽ Injury Project - Data Processing

## 📋 Project Overview

This project contains consolidated and processed data on athlete injuries from various leagues:
- **NBA** - professional male basketball players (ACL injuries)
- **WNBA** - professional female basketball players (ACL injuries)
- **Soccer** - professional soccer players (various injury types)
- **Collegiate** - student-athletes (ACL injury risk)

---

## 📁 Output Files

### 1. `injury_data_consolidated.xlsx`
Main data file containing **12 sheets**:

#### **Raw Data:**
- `NBA_Raw` - 120 rows, original NBA data
- `WNBA_Raw` - 60 rows, original WNBA data
- `Soccer_Raw` - 656 rows, original soccer data
- `Collegiate_Raw` - 200 rows, original collegiate data

#### **Processed Data:**
- `NBA_Processed` - NBA with additional columns and transformations
- `WNBA_Processed` - WNBA with additional columns and transformations
- `Soccer_Processed` - Soccer with injury categorization and metrics
- `Collegiate_Processed` - Collegiate with BMI, risk categories, etc.

#### **Combined Data:**
- `Basketball_Combined` - NBA + WNBA together (180 rows)

#### **Summaries:**
- `Summary_Basketball` - before/after stats for each player
- `Summary_Soccer` - stats per injury category
- `Summary_Collegiate` - stats per gender and risk category

### 2. `data_dictionary.xlsx`
Data dictionary describing all columns in the processed sheets.

### 3. `injury_data_processing.ipynb`
Jupyter Notebook with the full processing code (for future reference).

---

## 🔑 Key Transformations

### NBA / WNBA:
✅ **Split "made-attempted" columns:**
- `Field goals made-attempted per game` → `FG_made` + `FG_attempted`
- `Three-point field goals made-attempted per game` → `3PT_made` + `3PT_attempted`
- `Free throws made-attempted per game` → `FT_made` + `FT_attempted`

✅ **New columns:**
- `League` - NBA or WNBA
- `Injury_Type` - ACL (all injuries)
- `Period` - Summary Before / Summary After / Specific Season
- `Player_Name` - clean player name (without season)
- `GS_percent` - percentage of games started

### Soccer:
✅ **Injury categorization** - 13 categories:
- Knee - Cruciate Ligament (ACL)
- Knee - Other
- Muscle - Hamstring
- Muscle - Groin
- Muscle - Calf
- Muscle - Other
- Ankle
- Foot
- Hip
- Shoulder
- Hand
- Illness - Virus
- Fatigue
- Other

✅ **New metrics:**
- `Injury_Category` - categorized injury
- `Days_Absent` - number of days absent (Date of return - Date of Injury)
- `League` - Soccer

### Collegiate:
✅ **New health metrics:**
- `BMI` - Body Mass Index (weight / height²)
- `ACL_Risk_Category` - Low / Medium / High / Very High (based on ACL_Risk_Score)
- `Training_Load_Score` - Training_Intensity × Training_Hours_Per_Week
- `League` - Collegiate

---

## 📊 Data Statistics

### Number of athletes:
- **NBA**: 20 players with ACL injuries
- **WNBA**: 10 players with ACL injuries
- **Soccer**: 224 soccer players with various injuries
- **Collegiate**: 200 student-athletes

### NBA/WNBA Data Structure:
Each player has multiple rows:
- Season before injury (e.g., "Derrick Rose - 2009/10")
- Seasons after injury
- **"summary before"** - aggregated stats before injury
- **"summary after"** - aggregated stats after injury

### Top 5 Soccer Injuries:
1. Knee injury
2. Hamstring strain
3. Knee - Cruciate Ligament (ACL)
4. Muscle - Hamstring
5. Ankle injury

---

## 🎯 Analysis Possibilities

### 1. NBA vs WNBA Comparisons
```python
# Load data
df = pd.read_excel('injury_data_consolidated.xlsx', sheet_name='Basketball_Combined')

# Filter only summary
summary = df[df['Period'].isin(['Summary Before', 'Summary After'])]

# Compare average changes
summary.groupby(['League', 'Period'])['PTS'].mean()
```

### 2. Soccer Injury Analysis
```python
# Load data
df_soccer = pd.read_excel('injury_data_consolidated.xlsx', sheet_name='Soccer_Processed')

# Average time absent per injury
df_soccer.groupby('Injury_Category')['Days_Absent'].mean().sort_values(ascending=False)
```

### 3. Filtering ACL Injuries (all leagues)
```python
# NBA/WNBA - all are ACL
df_basketball = pd.read_excel('injury_data_consolidated.xlsx', sheet_name='Basketball_Combined')
acl_basketball = df_basketball[df_basketball['Injury_Type'] == 'ACL']

# Soccer - only ACL
df_soccer = pd.read_excel('injury_data_consolidated.xlsx', sheet_name='Soccer_Processed')
acl_soccer = df_soccer[df_soccer['Injury_Category'] == 'Knee - Cruciate Ligament']
```

### 4. Head-to-Head Comparison (e.g., Derrick Rose vs Klay Thompson)
```python
df = pd.read_excel('injury_data_consolidated.xlsx', sheet_name='NBA_Processed')

# Pick two players
players = ['Derrick Rose', 'Klay Thompson']
comparison = df[df['Player_Name'].isin(players)]

# Only summary before/after
summary = comparison[comparison['Period'].isin(['Summary Before', 'Summary After'])]

# Pivot for comparison
summary.pivot_table(values=['PTS', 'AST', 'REB'], 
                    index='Player_Name', 
                    columns='Period')
```

---

## 🔍 Important Columns

### Basketball (NBA/WNBA):
- **Player_Name** - filter by player
- **Period** - filter: "Summary Before" / "Summary After"
- **League** - filter: "NBA" / "WNBA"
- **PTS, AST, REB** - key stats
- **FG_made, FG_attempted, FG%** - shooting efficiency
- **Age during the injury** - age at time of injury
- **Recovery period** - recovery duration

### Soccer:
- **Name** - player name
- **Injury** - original injury name
- **Injury_Category** - categorized injury
- **Days_Absent** - days absent
- **Date of Injury, Date of return** - injury dates
- **Match1/2/3_before/after_injury** - match stats

### Collegiate:
- **Athlete_ID** - athlete ID
- **Gender** - gender
- **Position** - position (Guard/Forward/Center)
- **ACL_Risk_Score** - risk indicator (0-100)
- **ACL_Risk_Category** - Low/Medium/High/Very High
- **Injury_Indicator** - whether injury occurred (0/1)
- **BMI** - body mass index
- **Training_Load_Score** - training load

---

## 🚀 Next Steps (Data Analysis)

1. **Exploratory Data Analysis (EDA)**
   - Distributions of stats before/after injury
   - Correlations between variables
   - Outlier analysis

2. **Visualizations**
   - NBA vs WNBA comparisons (bar charts)
   - Radar charts for players (multi-dimensional)
   - Heatmaps of stat changes
   - Scatter plots (2D comparisons)

3. **Multivariate Analysis**
   - **PCA** (Principal Component Analysis) - dimensionality reduction
   - **Clustering** (K-means) - grouping players by recovery profile
   - **Classification** - predicting return to form

4. **Injury Comparisons**
   - ACL vs other injuries (Soccer)
   - Effect of age on return to form
   - Effect of recovery time on stats

---

## 💡 Tips for Working with the Data

### Missing Values:
- NBA/WNBA: some rows may have NaN in columns (e.g., season was incomplete)
- Soccer: some matches may have missing stats
- Collegiate: **no missing values** ✅

### Filtering Periods (NBA/WNBA):
```python
# Only summary rows (for before/after comparisons)
summary_only = df[df['Period'].isin(['Summary Before', 'Summary After'])]

# Only specific seasons (detailed analysis)
seasons_only = df[df['Period'] == 'Specific Season']
```

### Calculating Percentage Changes:
```python
# Example for Derrick Rose
player = df[df['Player_Name'] == 'Derrick Rose']
before = player[player['Period'] == 'Summary Before']['PTS'].values[0]
after = player[player['Period'] == 'Summary After']['PTS'].values[0]
change_pct = ((after - before) / before) * 100
print(f"Points change: {change_pct:.1f}%")
```

---

## 📞 Contact and Support

Questions? Issues? 
- Check `data_dictionary.xlsx` for column details
- See `injury_data_processing.ipynb` for processing code
- You can modify the notebook and reprocess the data

---

## ✅ Project Status

- [x] Loading raw data
- [x] Cleaning and transformation
- [x] Injury categorization
- [x] Consolidation to Excel
- [x] Creating summaries
- [x] Documentation
- [ ] **Data Analysis** - next step!

**Processed on:** 2026-02-01

---

**Good luck with the analysis! 🎉**
