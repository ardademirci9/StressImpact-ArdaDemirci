# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:00:27 2024

@author: Arda
"""

import json
from datetime import datetime
import pandas as pd

with open("izleme geçmişi.json", "r", encoding="utf-8") as file:
    data = json.load(file)

records = []
for item in data:
    if "header" in item and item["header"] == "YouTube Music":
        try:
            activity_time = datetime.fromisoformat(item["time"].replace("Z", "+00:00"))
            records.append({"date": activity_time.date(), "listening_time_minutes": 3})
        except Exception as e:
            pass

df = pd.DataFrame(records)

df = df[df["date"] >= datetime(2023, 10, 1).date()]

df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")

monthly_stats = (
    df.groupby("month")
    .agg(
        total_listening_time=("listening_time_minutes", "sum"),
        unique_days=("date", "nunique")
    )
    .reset_index()
)

monthly_stats["average_daily_listening_time"] = (
    monthly_stats["total_listening_time"] / monthly_stats["unique_days"]
)

monthly_stats["month"] = monthly_stats["month"].dt.strftime("%Y-%m")

output = monthly_stats[["month", "average_daily_listening_time"]].to_dict(orient="records")

with open("monthly_youtube_music_average.json", "w", encoding="utf-8") as output_file:
    json.dump(output, output_file, ensure_ascii=False, indent=4)
