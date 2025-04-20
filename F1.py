import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# F1 Driver Performance Data
drivers_data = {
    'Driver': ['Norris', 'Piastri', 'Verstappen', 'Russell', 'Leclerc', 'Antonelli', 'Hamilton', 'Albon', 'Ocon', 'Stroll',
               'Gasly', 'Hulkenberg', 'Bearman', 'Tsunoda',
                'Hadjar', 'Sainz', 'Alonso', 'Lawson', 'Doohan', 'Bortoleto'],

    'Team': ['McLaren Mercedes', 'McLaren Mercedes', 'Red Bull Racing Honda RBPT', 'Mercedes', 'Ferrari', 'Mercedes', 'Ferrari', 'Williams Mercedes', 'Haas Ferrari',
             'Aston Martin Aramco Mercedes', 'Alpine Renault',
             'Kick Sauber Ferrari', 'Haas Ferrari', 'Red Bull Racing Honda RBPT',
             'Racing Bulls Honda RBPT',
             'Williams Mercedes', 'Aston Martin Aramco Mercedes',
              'Racing Bulls Honda RBPT', 'Alpine Renault', 'Kick Sauber Ferrari'],

    'Points': [77, 74, 69, 63, 32, 30, 25, 18, 14, 10, 6, 6, 6, 5, 4, 1, 0, 0, 0, 0],
    'RacesCompleted': [4] * 20
}

# DataFrame creation
df = pd.DataFrame(drivers_data)

# Calculate predictions
total_races = 24
df['AvgPointsPerRace'] = df['Points'] / df['RacesCompleted']
df['RemainingRaces'] = total_races - df['RacesCompleted']
df['PredictedFinalPoints'] = df['Points'] + df['AvgPointsPerRace'] * df['RemainingRaces']
df_sorted = df.sort_values(by='PredictedFinalPoints', ascending=False)

# Visualization
plt.figure(figsize=(13, 8))
sns.set_style("whitegrid")
barplot = sns.barplot(
    data=df_sorted,
    x='PredictedFinalPoints',
    y='Driver',
    palette='cubehelix'
)

# Annotate predicted points next to bars
for index, row in df_sorted.iterrows():
    barplot.text(row['PredictedFinalPoints'] + 2, index, f"{round(row['PredictedFinalPoints'], 1)} pts", va='center')

plt.title("🔮 Predicted Final Points – F1 2025 Season", fontsize=18, fontweight='bold')
plt.xlabel("Predicted Final Points", fontsize=12)
plt.ylabel("Driver", fontsize=12)
plt.tight_layout()
plt.show()

# Terminal Output – Top 5 Drivers
top5 = df_sorted.head(5)

print("\n🌟 Top 5 Predicted Performers of the 2025 F1 Season:")
print("-" * 60)
for i, row in top5.iterrows():
    print(f"  {row['Driver']:10} | {row['Team'][:30]:30} | Predicted: {round(row['PredictedFinalPoints'], 2)} pts")

# Predicted Champion
champ = df_sorted.iloc[0]
print("\n🏆 Predicted 2025 World Champion:")
print(f"🎉 {champ['Driver']} from {champ['Team']} with {round(champ['PredictedFinalPoints'], 2)} points!")


