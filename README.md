# Gov_COVID_Spending_Analysis

**Forecasting U.S. Federal COVID Contract Spending**

This project analyzes U.S. federal spending related to COVID-19 using data from USAspending.gov. The goal was to identify spending patterns, explore time-series behavior, and present results through a Tableau dashboard.

The analysis includes data cleaning, exploratory analysis, rolling-average trend evaluation, and visualization of procurement activity across agencies, locations, and industries.

**Data Source**

Data was obtained from USAspending.gov, which provides publicly available records of federal contract awards. The raw dataset initially contained duplicate entries, which were removed during preprocessing.

Dataset characteristics:
  *Time range: 2019–2026
  *Award type: Prime awards
  *Key variables:
    *award_latest_action_date
    *total_obligated_amount
    *funding_agency_name
    *primary_place_of_performance_state_name 
    *naics_description
    *award_type
    *recipient_name

**Data Processing Pipeline**

Python was used for data cleaning and transformation before visualization.

The analysis pipeline included the following steps:
  *Import and combine raw CSV datasets
  *Filter unnecessary columns
  *Remove duplicate contract entries (~8,000 records)
  *Convert date and numeric data types
  *Aggregate contract spending by month
  *Create derived features for time-series analysis
  *Export processed data for visualization

**Exploratory Analysis**

Exploratory analysis focused on identifying temporal patterns in federal COVID-19 spending.

Techniques used:
  *Monthly aggregation of obligated spending
  *6-month rolling average to smooth volatility
  *Visual inspection of spending spikes and anomalies

The results showed that spending behavior was dominated by large episodic spikes rather than consistent long-term trends, making conventional forecasting approaches unreliable.

**Visualization Dashboard**

The processed dataset was used to build an interactive Tableau dashboard displaying:
  *Monthly federal COVID contract spending
  *Spending by funding agency
  *Contract recipients
  *Geographic distribution of contract activity
  *Industry breakdown using NAICS classifications

**Key Findings**

*COVID procurement spending occurred in large bursts rather than steady growth
*Spending was concentrated within a small number of federal agencies
*Certain industries showed rapid temporary procurement surges
*These patterns suggest pandemic procurement operated through episodic emergency contracting waves rather than stable funding streams.

**Tools Used**

*Python
*pandas
*Matplotlib
*numpy
*Tableau
*USAspending.gov data
