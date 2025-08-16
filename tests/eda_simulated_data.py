# %% EDA to test out quality of simulated data

## Dependencies
import pandas as pd
import dtale
from analytics_tasks_utils.reporting import eda_snapshot
from analytics_tasks_utils.text import clean_text_df, pos_tags_df
from ydata_profiling import ProfileReport

## Simulated data
"""
Start Date: 01-01-2022
End Date: 14-08-2025
Severity Distribution: Realistic
Seasonal Patterns: Random distribution
"""
df = pd.read_json(r"C:\Users\Ashut\Downloads\customer_complaints_100000_records.json")
df.head(2).T

# %% EDA

## Shape
df.shape

## Formatting
df['customer_dob'] = pd.to_datetime(df['customer_dob'])
df['complaint_interaction_date'] = pd.to_datetime(df['complaint_interaction_date'])


## EDA snapshot
eda_snapshot(df)

## dtale
d = dtale.show(df)
d.open_browser()

## Profile report
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("your_report.html")

## Specific columns
df.customer_country.value_counts()

df.customer_age_group.value_counts()

df.complaint_mode.value_counts()

df.drug_class.value_counts()


## Resampling: complaint_interaction_date
df.groupby(df["complaint_interaction_date"].dt.year)["customer_id"].nunique().reset_index() #yr
df.groupby(df["complaint_interaction_date"].dt.to_period("Q"))["customer_id"].nunique().reset_index() #qtr
df.groupby(df["complaint_interaction_date"].dt.to_period("M"))["customer_id"].nunique().reset_index() #mt
df.groupby(df["complaint_interaction_date"].dt.to_period("W"))["customer_id"].nunique().reset_index() #wk

## Resampling: customer_dob
df.groupby(df["customer_dob"].dt.year)["customer_id"].nunique().reset_index() #yr


## Clean
df = clean_text_df(df, 'complaint_desc_narrative')
df.head(2).T


## POS tags
df = clean_text_df(df, 'complaint_desc_narrative')
df.head(2).T







