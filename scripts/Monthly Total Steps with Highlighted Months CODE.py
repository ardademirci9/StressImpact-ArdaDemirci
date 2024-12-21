import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the file
with open(r'C:\Users\Arda\Desktop\DSA PROJECT\step count\daily_step_counts_from_oct_2023.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)

if 'totalSteps' in df.columns:
    df.rename(columns={'totalSteps': 'steps'}, inplace=True)
else:
    raise KeyError("The key 'totalSteps' was not found in the JSON file!")

df['date'] = pd.to_datetime(df['date'])

df.sort_values('date', inplace=True)

# Calculate monthly total step counts
df['month'] = df['date'].dt.to_period('M')  # Add month column (e.g., 2023-11)
monthly_steps = df.groupby('month')['steps'].sum().reset_index()

monthly_steps['month'] = monthly_steps['month'].dt.to_timestamp()

exam_months = ['2023-11', '2024-01', '2024-03', '2024-05', '2024-11']
monthly_steps['color'] = monthly_steps['month'].dt.strftime('%Y-%m').apply(
    lambda x: 'red' if x in exam_months else 'skyblue'
)

plt.figure(figsize=(16, 8))
plt.bar(
    monthly_steps['month'],
    monthly_steps['steps'],
    color=monthly_steps['color'],
    edgecolor='black',
    width=20
)

# plot çiz
plt.title('Monthly Total Steps with Highlighted Exam Months', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Steps', fontsize=14)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
