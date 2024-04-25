import pandas as pd
import numpy as np

# Read Excel file
data_schiller = pd.read_excel("ie_data.xls", sheet_name="Data", header=None)

# Drop the first 7 rows and certain columns
data_schiller = data_schiller.drop(data_schiller.index[0:7]).reset_index(drop=True)
data_schiller = data_schiller.drop(columns=[1, 14, 16])

# Set column names
data_schiller.columns = ['Date', 'S&P Comp', 'Dividend', 'Earnings', 'Consumer Price CPI', 
                             'Date Fraction', 'Long Interest Rate', 'Real price', 'Real Dividend', 
                             'Real Total Return Price', 'Real Earnings','Real TR Scaled Earnings', 
                             'CAPE', 'TR CAPE', 'Excess CAPE Yield', 'Monthly Total Bond Returns', 
                             'Real Total Bond Returns', '10 Years Annualized Stock Real Return', 
                             '10 Years Annualized Bonds Real Return', 'Real 10 Years excess Annualized Returns'
                          ]
# Convert columns 2 to 20 to numeric and the Date column to string

data_schiller.iloc[:, 1:20] = data_schiller.iloc[:, 1:20].apply(pd.to_numeric, errors='coerce')
data_schiller['Date'] = data_schiller['Date'].astype(str)

# Extract year and quarter from the Date, then form a new Date format
year = data_schiller['Date'].str.slice(0, 4)
quarter = data_schiller['Date'].str.slice(5, 7)
date = year + "-" + quarter + "-01"
data_schiller['Date'] = pd.to_datetime(date, errors='coerce')

# Drop rows where Date is NA
data_schiller = data_schiller.dropna(subset=['Date'])

data_schiller['Date', 'S&P Comp', 'Dividend', 'Earnings', 'Consumer Price CPI', 
                             'Real price', 'Real Dividend', 
                             'Real Total Return Price', 'Real Earnings', 
                             'CAPE', '10 Years Annualized Stock Real Return', 
                             
                          ].head()
