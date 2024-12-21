# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:30:23 2024

@author: Arda
"""

import pandas as pd

# JSON dosyasını yükle
steps_data = pd.read_json("C:\\Users\\Arda\\Desktop\\DSA PROJECT\\daily_step_counts_from_oct_2023.json")

# Tarih sütununu datetime formatına dönüştür
steps_data['date'] = pd.to_datetime(steps_data['date'])

# 2024 ve sonrasına filtrele
steps_data = steps_data[steps_data['date'] >= "2024-01-01"]

# Aylık toplam adım sayılarını hesapla
steps_data['month'] = steps_data['date'].dt.to_period('M')
monthly_steps = steps_data.groupby('month')['totalSteps'].sum().reset_index()

# 'month' sütununu string formatına çevir
monthly_steps['month'] = monthly_steps['month'].astype(str)

output_path = "C:\\Users\\Arda\\Desktop\\DSA PROJECT\\monthly_step_counts_2024.json"
monthly_steps.to_json(output_path, orient='records', indent=4)

print(f"Aylık toplam adım sayıları {output_path} dosyasına kaydedildi.")
