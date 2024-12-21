import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

steps_data = pd.read_json("C:\\Users\\Arda\\Desktop\\DSA PROJECT\\monthly_step_counts_2024.json")
music_data = pd.read_json("C:\\Users\\Arda\\Desktop\\DSA PROJECT\\monthly_youtube_music_average.json")

steps_data['month'] = pd.to_datetime(steps_data['month'])
music_data['month'] = pd.to_datetime(music_data['month'])

merged_data = pd.merge(steps_data, music_data, on='month', how='inner')
merged_data.rename(columns={'totalSteps': 'step_count', 'average_daily_listening_time': 'music_time'}, inplace=True)

plt.figure(figsize=(10, 6))
plt.scatter(merged_data['step_count'], merged_data['music_time'], alpha=0.7, color='blue')
plt.title('Relationship Between Monthly Step Count and Music Listening Time', fontsize=14)
plt.xlabel('Monthly Step Count', fontsize=12)
plt.ylabel('Music Listening Time (minutes)', fontsize=12)
plt.grid(True)

correlation, _ = pearsonr(merged_data['step_count'], merged_data['music_time'])
plt.figtext(0.15, 0.8, f"Pearson Correlation: {correlation:.2f}", fontsize=12, color="red")

plt.tight_layout()
plt.show()
