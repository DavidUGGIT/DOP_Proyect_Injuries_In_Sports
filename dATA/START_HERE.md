#  START HERE - Injury Project


This is a complete data package for the athlete injury analysis project.  
**Read this file first — it will only take 2 minutes!**

---

##  What's in this package?

### 1️⃣ **DATA (the most important!):**
- `injury_data_consolidated.xlsx` - **main data file** (12 sheets)
- `data_dictionary.xlsx` - description of all columns

### 2️⃣ **DOCUMENTATION:**
- `README.md` - detailed project documentation
- `RAW_vs_PROCESSED_guide.md` - differences between raw and processed data
- `code_examples.md` - ready-to-use code snippets

### 3️⃣ **JUPYTER NOTEBOOKS:**
- `quick_start_guide.ipynb` - **start here!** Analysis examples
- `injury_data_processing.ipynb` - full processing code (optional)

---

##  How to get started? (3 steps)

### STEP 1: Install the required libraries

Open your terminal/command prompt and type:

```bash
pip install pandas numpy matplotlib seaborn openpyxl jupyter
```

*(If you already have these libraries, skip this step)*

---

### STEP 2: Open a notebook

**OPTION A - Jupyter Notebook (easier):**
```bash
jupyter notebook
```
Then open: `quick_start_guide.ipynb`

**OPTION B - Python directly:**
Create a new `.py` file and copy code from `code_examples.md`

---

### STEP 3: Load data and start analyzing!

```python
import pandas as pd

# Load data (USE PROCESSED, NOT RAW!)
df_nba = pd.read_excel('injury_data_consolidated.xlsx', 
                        sheet_name='NBA_Processed')

# You can start analyzing right away!
print(df_nba.head())
```

**That's it!** You're ready to go! 🎉

---

##  What data do you have?

### Basketball (NBA + WNBA):
- **20 NBA players** with ACL injuries
- **10 WNBA players** with ACL injuries
- Stats before and after injury
- NBA vs WNBA comparisons available

### Soccer:
- **224 soccer players** with various injuries
- **13 injury categories** (ACL, Hamstring, Ankle, etc.)
- Information on time out

### Collegiate:
- **200 student-athletes**
- ACL injury risk indicators
- Training and health data

---


##  What can we do with this data?

### Basic analyses:
✅ Compare a player before and after injury  
✅ Compare NBA vs WNBA  
✅ Analyze different injury types (Soccer)  
✅ Filter by players, leagues, injuries  
✅ Create charts and visualizations  

### Advanced analyses:
✅ PCA (dimensionality reduction)  
✅ Clustering (grouping players)  
✅ Radar charts (multi-dimensional comparisons)  
✅ Heatmaps of stat changes  
✅ Predicting return to form  

---

### Example 1: Compare a player before/after
```python
import pandas as pd

df = pd.read_excel('injury_data_consolidated.xlsx', 
                   sheet_name='NBA_Processed')

# Pick a player
player = df[df['Player_Name'] == 'Derrick Rose']

# Only before/after
before = player[player['Period'] == 'Summary Before'].iloc[0]
after = player[player['Period'] == 'Summary After'].iloc[0]

# Compare
print(f"PTS: {before['PTS']} → {after['PTS']}")
print(f"AST: {before['AST']} → {after['AST']}")
print(f"REB: {before['REB']} → {after['REB']}")
```

### Example 2: NBA vs WNBA
```python
df = pd.read_excel('injury_data_consolidated.xlsx', 
                   sheet_name='Basketball_Combined')

# Only summary
summary = df[df['Period'].isin(['Summary Before', 'Summary After'])]

# Averages per league
avg = summary.groupby(['League', 'Period'])['PTS'].mean()
print(avg)
```

### Example 3: Top Soccer injuries
```python
df = pd.read_excel('injury_data_consolidated.xlsx', 
                   sheet_name='Soccer_Processed')

# Most common injuries
top = df['Injury_Category'].value_counts().head(10)
print(top)
```

**More examples:** See `code_examples.md` or `quick_start_guide.ipynb`!

---