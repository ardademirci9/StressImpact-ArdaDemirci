import pandas as pd
import matplotlib.pyplot as plt
import json


with open("monthly_youtube_music_average.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)
df["month"] = pd.to_datetime(df["month"])

exam_months = df["month"].dt.month.isin([3, 5, 11, 1])


plt.figure(figsize=(12, 6))
plt.scatter(df["month"], df["average_daily_listening_time"], color="blue", edgecolor="black", s=100, label="Regular Months")
plt.scatter(df["month"][exam_months], df["average_daily_listening_time"][exam_months], color="red", edgecolor="black", s=100, label="Exam Months")

plt.plot(df["month"], df["average_daily_listening_time"], linestyle="-", color="blue", alpha=0.7)

plt.title("Average Daily Music Listening Time by Month", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Daily Listening Time (minutes)", fontsize=12)
plt.xticks(df["month"], df["month"].dt.strftime("%Y-%m"), rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)

plt.legend(fontsize=10)
plt.tight_layout()

plt.show()
