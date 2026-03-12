#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:17:41 2026

@author: tobyh1
"""

import pandas as pd

df=pd.read_csv('reduced_data.csv')

# Convert dates to correct data type
df["award_latest_action_date"] = pd.to_datetime(
    df["award_latest_action_date"],
    errors="coerce"
)

# Convert dates from day resolution to month resolution
df["action_year_month"] = df["award_latest_action_date"].dt.to_period("M")

# Calculate monthly spending
monthly_spending = (
    df.groupby("action_year_month")["total_obligated_amount"]
    .sum()
    .reset_index()
)

# Convert action_year_month back to timestamp
monthly_spending["action_year_month"] = monthly_spending["action_year_month"].dt.to_timestamp()

df.to_csv("cleaned_data.csv", index=False)

monthly_spending["t"] = range(len(monthly_spending))

monthly_spending.to_csv("monthly_spending.csv", index=False)