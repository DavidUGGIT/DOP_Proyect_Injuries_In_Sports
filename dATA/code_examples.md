# 📚 Code Examples - Ready-to-Use Snippets

## Table of Contents
1. [Loading Data](#1-loading-data)
2. [Filtering](#2-filtering)
3. [Before/After Comparisons](#3-beforeafter-comparisons)
4. [NBA vs WNBA Comparisons](#4-nba-vs-wnba-comparisons)
5. [Soccer Analysis](#5-soccer-analysis)
6. [Visualizations](#6-visualizations)
7. [Exporting Results](#7-exporting-results)

---

## 1. Loading Data

### Load all processed sheets
```python
import pandas as pd

FILE = 'injury_data_consolidated.xlsx'

df_nba = pd.read_excel(FILE, sheet_name='NBA_Processed')
df_wnba = pd.read_excel(FILE, sheet_name='WNBA_Processed')
df_basketball = pd.read_excel(FILE, sheet_name='Basketball_Combined')
df_soccer = pd.read_excel(FILE, sheet_name='Soccer_Processed')
df_collegiate = pd.read_excel(FILE, sheet_name='Collegiate_Processed')
```

### Load only summaries
```python
summary_basketball = pd.read_excel(FILE, sheet_name='Summary_Basketball')
summary_soccer = pd.read_excel(FILE, sheet_name='Summary_Soccer')
summary_collegiate = pd.read_excel(FILE, sheet_name='Summary_Collegiate')
```

---

## 2. Filtering

### Filter by player (NBA/WNBA)
```python
player_name = 'Derrick Rose'
player_data = df_nba[df_nba['Player_Name'] == player_name]
```

### Filter by Period (only before/after)
```python
summary_only = df_nba[df_nba['Period'].isin(['Summary Before', 'Summary After'])]
```

### Filter by league
```python
# Only NBA from combined
nba_only = df_basketball[df_basketball['League'] == 'NBA']

# Only WNBA
wnba_only = df_basketball[df_basketball['League'] == 'WNBA']
```

### Filter Soccer by injury category
```python
# Only ACL
acl_only = df_soccer[df_soccer['Injury_Category'] == 'Knee - Cruciate Ligament']

# Only muscle injuries
muscle_injuries = df_soccer[df_soccer['Injury_Category'].str.contains('Muscle')]

# Only knee injuries (all types)
knee_injuries = df_soccer[df_soccer['Injury_Category'].str.contains('Knee')]
```

### Filter Collegiate by risk
```python
# High ACL risk
high_risk = df_collegiate[df_collegiate['ACL_Risk_Category'] == 'Very High']

# High + Very High combined
high_combined = df_collegiate[df_collegiate['ACL_Risk_Category'].isin(['High', 'Very High'])]
```

---

## 3. Before/After Comparisons

### One player - before vs after
```python
player_name = 'Derrick Rose'

# Extract data
before = df_nba[(df_nba['Player_Name'] == player_name) & 
                (df_nba['Period'] == 'Summary Before')].iloc[0]
after = df_nba[(df_nba['Player_Name'] == player_name) & 
               (df_nba['Period'] == 'Summary After')].iloc[0]

# Compare stats
stats = ['PTS', 'AST', 'REB', 'FG%', '3PT%']
for stat in stats:
    b = before[stat]
    a = after[stat]
    if pd.notna(b) and pd.notna(a) and b != 0:
        change = ((a - b) / b) * 100
        print(f"{stat:10s}: {b:6.2f} → {a:6.2f} ({change:+6.1f}%)")
```

### All players - average change
```python
# Only summary
summary = df_nba[df_nba['Period'].isin(['Summary Before', 'Summary After'])]

# Pivot: each player has before and after
pivot = summary.pivot_table(
    values=['PTS', 'AST', 'REB'],
    index='Player_Name',
    columns='Period'
)

# Calculate changes
for stat in ['PTS', 'AST', 'REB']:
    before_vals = pivot[stat]['Summary Before']
    after_vals = pivot[stat]['Summary After']
    changes = ((after_vals - before_vals) / before_vals * 100)
    
    print(f"\n{stat} - Average change: {changes.mean():.1f}%")
    print(f"Min: {changes.min():.1f}%, Max: {changes.max():.1f}%")
```

### Comparison table for multiple players
```python
players = ['Derrick Rose', 'Klay Thompson', 'Zach LaVine']

rows = []
for player in players:
    p_data = df_nba[
        (df_nba['Player_Name'] == player) & 
        (df_nba['Period'].isin(['Summary Before', 'Summary After']))
    ]
    
    before = p_data[p_data['Period'] == 'Summary Before'].iloc[0]
    after = p_data[p_data['Period'] == 'Summary After'].iloc[0]
    
    row = {
        'Player': player,
        'PTS_before': before['PTS'],
        'PTS_after': after['PTS'],
        'PTS_change%': ((after['PTS'] - before['PTS']) / before['PTS'] * 100) if before['PTS'] > 0 else None,
        'AST_before': before['AST'],
        'AST_after': after['AST'],
        'REB_before': before['REB'],
        'REB_after': after['REB']
    }
    rows.append(row)

comparison_table = pd.DataFrame(rows)
print(comparison_table.round(2))
```

---

## 4. NBA vs WNBA Comparisons

### Average stats per league
```python
summary = df_basketball[df_basketball['Period'].isin(['Summary Before', 'Summary After'])]

# Averages before/after for each league
avg_by_league = summary.groupby(['League', 'Period'])[
    ['PTS', 'AST', 'REB', 'FG%', '3PT%']
].mean()

print(avg_by_league.round(2))
```

### Percentage changes NBA vs WNBA
```python
import numpy as np

for league in ['NBA', 'WNBA']:
    league_data = df_basketball[df_basketball['League'] == league]
    summary = league_data[league_data['Period'].isin(['Summary Before', 'Summary After'])]
    
    pivot = summary.pivot_table(
        values=['PTS', 'AST', 'REB'],
        index='Player_Name',
        columns='Period'
    )
    
    print(f"\n{league}:")
    for stat in ['PTS', 'AST', 'REB']:
        before_vals = pivot[stat]['Summary Before']
        after_vals = pivot[stat]['Summary After']
        changes = ((after_vals - before_vals) / before_vals * 100)
        print(f"  {stat}: average change {changes.mean():.1f}%")
```

### Test which league recovers better
```python
def calculate_avg_change(df, league):
    league_data = df[df['League'] == league]
    summary = league_data[league_data['Period'].isin(['Summary Before', 'Summary After'])]
    
    pivot = summary.pivot_table(
        values=['PTS', 'AST', 'REB'],
        index='Player_Name',
        columns='Period'
    )
    
    changes = {}
    for stat in ['PTS', 'AST', 'REB']:
        before_vals = pivot[stat]['Summary Before']
        after_vals = pivot[stat]['Summary After']
        changes[stat] = ((after_vals - before_vals) / before_vals * 100).mean()
    
    return changes

nba_changes = calculate_avg_change(df_basketball, 'NBA')
wnba_changes = calculate_avg_change(df_basketball, 'WNBA')

print("Average changes:")
print(f"NBA:  PTS={nba_changes['PTS']:.1f}%, AST={nba_changes['AST']:.1f}%, REB={nba_changes['REB']:.1f}%")
print(f"WNBA: PTS={wnba_changes['PTS']:.1f}%, AST={wnba_changes['AST']:.1f}%, REB={wnba_changes['REB']:.1f}%")
```

---

## 5. Soccer Analysis

### Top 10 most common injuries
```python
top_injuries = df_soccer['Injury_Category'].value_counts().head(10)
print(top_injuries)
```

### Average time absent per injury
```python
avg_absence = df_soccer.groupby('Injury_Category')['Days_Absent'].agg([
    'mean', 'median', 'min', 'max', 'count'
]).sort_values('mean', ascending=False)

print(avg_absence.round(1))
```

### Comparing ACL with other knee injuries
```python
knee_injuries = df_soccer[df_soccer['Injury_Category'].str.contains('Knee')]

avg_by_knee_type = knee_injuries.groupby('Injury_Category')['Days_Absent'].agg([
    'mean', 'count'
]).sort_values('mean', ascending=False)

print("Knee injuries - average time absent:")
print(avg_by_knee_type.round(1))
```

### Injuries by age
```python
# Add age group
df_soccer['Age_Group'] = pd.cut(
    df_soccer['Age'], 
    bins=[0, 25, 30, 35, 100],
    labels=['<25', '25-30', '30-35', '35+']
)

age_analysis = df_soccer.groupby('Age_Group')['Days_Absent'].agg([
    'mean', 'median', 'count'
])

print("Time absent by age group:")
print(age_analysis.round(1))
```

---

## 6. Visualizations

### Bar chart - before vs after (one player)
```python
import matplotlib.pyplot as plt
import numpy as np

player_name = 'Derrick Rose'
before = df_nba[(df_nba['Player_Name'] == player_name) & 
                (df_nba['Period'] == 'Summary Before')].iloc[0]
after = df_nba[(df_nba['Player_Name'] == player_name) & 
               (df_nba['Period'] == 'Summary After')].iloc[0]

stats = ['PTS', 'AST', 'REB']
before_vals = [before[s] for s in stats]
after_vals = [after[s] for s in stats]

x = np.arange(len(stats))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, before_vals, width, label='Before', color='steelblue')
ax.bar(x + width/2, after_vals, width, label='After', color='coral')

ax.set_ylabel('Value per game')
ax.set_title(f'{player_name} - Before vs After ACL')
ax.set_xticks(x)
ax.set_xticklabels(stats)
ax.legend()
plt.show()
```

### Heatmap of changes (multiple players)
```python
import seaborn as sns

# Pick players
players = ['Derrick Rose', 'Klay Thompson', 'Zach LaVine', 'Klay Thompson']

# Calculate changes
changes_data = []
for player in players:
    p_data = df_nba[
        (df_nba['Player_Name'] == player) & 
        (df_nba['Period'].isin(['Summary Before', 'Summary After']))
    ]
    if len(p_data) == 2:
        before = p_data[p_data['Period'] == 'Summary Before'].iloc[0]
        after = p_data[p_data['Period'] == 'Summary After'].iloc[0]
        
        row = {'Player': player}
        for stat in ['PTS', 'AST', 'REB', 'FG%', '3PT%']:
            if before[stat] > 0:
                row[stat] = ((after[stat] - before[stat]) / before[stat] * 100)
            else:
                row[stat] = 0
        changes_data.append(row)

changes_df = pd.DataFrame(changes_data).set_index('Player')

# Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(changes_df, annot=True, fmt='.1f', cmap='RdYlGn', center=0, 
            cbar_kws={'label': '% change'})
plt.title('Stat changes after ACL injury')
plt.tight_layout()
plt.show()
```

### Scatter plot (2D)
```python
# Prepare data
summary = df_nba[df_nba['Period'].isin(['Summary Before', 'Summary After'])]
pivot = summary.pivot_table(
    values=['PTS', 'AST'],
    index='Player_Name',
    columns='Period'
)

pts_change = ((pivot['PTS']['Summary After'] - pivot['PTS']['Summary Before']) / 
              pivot['PTS']['Summary Before'] * 100)
ast_change = ((pivot['AST']['Summary After'] - pivot['AST']['Summary Before']) / 
              pivot['AST']['Summary Before'] * 100)

# Chart
plt.figure(figsize=(10, 8))
plt.scatter(pts_change, ast_change, s=100, alpha=0.6)

for player in pts_change.index:
    plt.annotate(player, (pts_change[player], ast_change[player]), 
                fontsize=8, alpha=0.7)

plt.axhline(0, color='gray', linestyle='--', alpha=0.5)
plt.axvline(0, color='gray', linestyle='--', alpha=0.5)
plt.xlabel('% change PTS')
plt.ylabel('% change AST')
plt.title('Scatter plot: Points change vs Assists change')
plt.grid(alpha=0.3)
plt.show()
```

### Box plot - time absent Soccer
```python
# Top 5 injuries
top5 = df_soccer['Injury_Category'].value_counts().head(5).index
data_top5 = df_soccer[df_soccer['Injury_Category'].isin(top5)]

plt.figure(figsize=(12, 6))
data_top5.boxplot(column='Days_Absent', by='Injury_Category', figsize=(12, 6))
plt.title('Distribution of time absent for top 5 injuries')
plt.suptitle('')
plt.ylabel('Days absent')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

---

## 7. Exporting Results

### Save results to CSV
```python
# Example: comparison table
comparison_table.to_csv('comparison_results.csv', index=False)
print("✅ Saved to comparison_results.csv")
```

### Save to Excel with multiple sheets
```python
with pd.ExcelWriter('my_analysis_results.xlsx') as writer:
    comparison_table.to_excel(writer, sheet_name='Player Comparison', index=False)
    avg_by_league.to_excel(writer, sheet_name='League Averages')
    top_injuries.to_frame().to_excel(writer, sheet_name='Soccer Injuries')

print("✅ Saved to my_analysis_results.xlsx")
```

### Save a chart
```python
# After creating a chart
plt.savefig('player_comparison.png', dpi=300, bbox_inches='tight')
print("✅ Saved chart to player_comparison.png")
```

---

## 💡 Additional Snippets

### List all NBA players
```python
players_nba = df_nba[df_nba['Period'] == 'Summary Before']['Player_Name'].tolist()
print(f"NBA Players ({len(players_nba)}):")
for i, player in enumerate(players_nba, 1):
    print(f"  {i:2d}. {player}")
```

### Descriptive statistics
```python
# For one stat
print(df_nba['PTS'].describe())

# For multiple
print(df_nba[['PTS', 'AST', 'REB']].describe())
```

### Correlations between stats
```python
# Only numeric data
numeric_cols = ['PTS', 'AST', 'REB', 'FG%', '3PT%', 'FT%']
correlation = df_nba[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlations between stats')
plt.tight_layout()
plt.show()
```

---

**Copy and paste the snippets you need into your code! 🚀**
