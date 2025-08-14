# %% EDA to test out quality of simulated data

## Dependencies
import pandas as pd
import dtale
from drug_complaint_parser.utils.eda_snapshot import eda_snapshot


## Simulated data
"""
Start Date: 01-01-2022
End Date: 14-08-2025
Severity Distribution: Realistic
Seasonal Patterns: Random distribution
"""
df = pd.read_json(r"C:\Users\Ashut\Downloads\customer_complaints_100000_records.json")
df.head(2).T
df.shape
df.info()

df.customer_country.value_counts()

df.customer_age_group.value_counts()

df.complaint_mode.value_counts()

df.drug_class.value_counts()

## eda_snapshot
eda_snapshot(df)

## dtale
d = dtale.show(df)
d.open_browser()
