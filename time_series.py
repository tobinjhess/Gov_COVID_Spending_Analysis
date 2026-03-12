#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:28:16 2026

@author: tobyh1
"""

import pandas as pd

monthly_spending=pd.read_csv('monthly_spending.csv')

# Convert dates to correct data type
monthly_spending["action_year_month"] = pd.to_datetime(
    monthly_spending["action_year_month"],
    errors="coerce"
)

# plotting spending over time
import matplotlib.pyplot as plt

plt.figure()
plt.plot(
    monthly_spending["action_year_month"],
    monthly_spending["total_obligated_amount"]
)
plt.title("Monthly COVID Contract Spending")
plt.xlabel("Month")
plt.ylabel("Total Obligated Amount")
plt.show()

# plot log scale
import numpy as np

plt.figure()
plt.plot(
    monthly_spending["action_year_month"],
    np.log1p(monthly_spending["total_obligated_amount"])
)
plt.title("Log Monthly COVID Contract Spending")
plt.show()

# calculate rolling average
monthly_spending["rolling_mean"] = (
    monthly_spending["total_obligated_amount"]
    .rolling(6)
    .mean()
)

# plotting spending over time compared to 6 month average
plt.figure()
plt.plot(
    monthly_spending["action_year_month"],
    monthly_spending["total_obligated_amount"]
)
plt.plot(
    monthly_spending["action_year_month"],
    monthly_spending["rolling_mean"]
)
plt.title("Monthly COVID Contract Spending vs. 6-Month Rolling Average")
plt.xlabel("Month")
plt.ylabel("Total Obligated Amount")
plt.legend(["Monthly COVID Spending", "6-Month Average"])
plt.show()

# Autocorrelation plots
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(monthly_spending["total_obligated_amount"], lags=24)
plt.show()

rolling_series = monthly_spending["rolling_mean"].dropna()

plot_acf(rolling_series, lags=24)
plt.show()



