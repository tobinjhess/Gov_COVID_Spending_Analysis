#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 16:21:23 2026

@author: tobyh1
"""

import pandas as pd

files = ['/Users/tobyh1/Gov_COVID_Spending/Data/PrimeAwardSummariesAndSubawards_2026-02-25_H18M37S35139579_2020/Contracts_PrimeAwardSummaries_2026-02-25_H18M42S42_1.csv',
         '/Users/tobyh1/Gov_COVID_Spending/Data/PrimeAwardSummariesAndSubawards_2026-02-25_H19M01S18654835_2021/Contracts_PrimeAwardSummaries_2026-02-25_H19M01S23_1.csv',
         '/Users/tobyh1/Gov_COVID_Spending/Data/PrimeAwardSummariesAndSubawards_2026-02-25_H19M03S08102334_2022/Contracts_PrimeAwardSummaries_2026-02-25_H19M03S11_1.csv',
         '/Users/tobyh1/Gov_COVID_Spending/Data/PrimeAwardSummariesAndSubawards_2026-02-25_H19M04S39241208_2023/Contracts_PrimeAwardSummaries_2026-02-25_H19M04S41_1.csv',
         '/Users/tobyh1/Gov_COVID_Spending/Data/PrimeAwardSummariesAndSubawards_2026-02-25_H19M07S56738868_2024/Contracts_PrimeAwardSummaries_2026-02-25_H19M07S58_1.csv',
         '/Users/tobyh1/Gov_COVID_Spending/Data/PrimeAwardSummariesAndSubawards_2026-02-25_H19M11S22032779_2025/Contracts_PrimeAwardSummaries_2026-02-25_H19M11S23_1.csv',
         '/Users/tobyh1/Gov_COVID_Spending/Data/PrimeAwardSummariesAndSubawards_2026-02-25_H19M14S30293461_2026/Contracts_PrimeAwardSummaries_2026-02-25_H19M21S10_1.csv',
    ]

dfs = [pd.read_csv(file) for file in files]

combined_df = pd.concat(dfs, ignore_index=True)

# obligated_amount_from_COVID-19_supplementals (only disaster relief)
# total_obligated_amount (total COVID expenditure including normal spending)
# award_base_action_date
# awarding_agency_name, awarding_sub_agency_name, funding_agency_name (focus on this one)
# primary_place_of_performance_state_name (use this), recipient_state_name
# naics_code, naics_description
# award_type, award_type_code

columns = [
    "award_latest_action_date",
    "total_obligated_amount",
    "funding_agency_name",
    "primary_place_of_performance_state_name",
    "naics_description",
    "award_type",
    "recipient_name",
    "contract_award_unique_key"
]

df_reduced = combined_df[columns]

# drop duplicates
df_reduced = df_reduced.drop_duplicates(
    subset=[
        "contract_award_unique_key",
        "award_latest_action_date",
        "total_obligated_amount"
    ]
)

combined_df.to_csv("combined_data.csv", index=False)

df_reduced.to_csv("reduced_data.csv", index=False)

