
Created on Mon Nov 25 17:03:40 2024

@author: Arda
"""

import pandas as pd
import json
from datetime import datetime


input_file = "step_count_data.json"
output_file = "daily_step_counts_from_oct_2023.json"

with open(input_file, "r", encoding="utf-8") as f:
    step_data = json.load(f)


df = pd.DataFrame(step_data)


df["value"] = pd.to_numeric(df["value"], errors="coerce")

df["startDate"] = pd.to_datetime(df["startDate"], format="%Y-%m-%d %H:%M:%S %z", errors="coerce")
df["date"] = df["startDate"].dt.date


start_filter_date = datetime(2023, 10, 1).date()
df_filtered = df[df["date"] >= start_filter_date]

daily_steps = df_filtered.groupby("date")["value"].sum().reset_index()
daily_steps.rename(columns={"value": "totalSteps"}, inplace=True)


daily_steps.to_json(output_file, orient="records", date_format="iso", indent=4)

print(f"Daily step counts from October 2023 saved to {output_file}")
