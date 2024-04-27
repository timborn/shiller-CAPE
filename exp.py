import pandas as pd
import numpy as np
import sys

# process mandatory command line option:
# $0 [CAPE|CDATE] 
if len(sys.argv) < 2:
  print("Error: mandatory command line choice:")
  print("  CAPE - if you want the CAPE number")
  print("  CDATE - date of that CAPE number, to make sure it's fresh")
  exit(1)

# Read Excel file
data_shiller = pd.read_excel("ie_data.xls", sheet_name="Data", header=None)

# Drop the first 8 rows and certain columns
data_shiller = data_shiller.drop(data_shiller.index[0:8]).reset_index(drop=True)
# data_shiller = data_shiller.drop(columns=[1, 14, 16])
data_shiller = data_shiller.drop(columns=[13, 15])

# Set column names
data_shiller.columns = ['Date', 'S&P Comp', 'Dividend', 'Earnings', 'Consumer Price CPI', 
                             'Date Fraction', 'Long Interest Rate', 'Real price', 'Real Dividend', 
                             'Real Total Return Price', 'Real Earnings','Real TR Scaled Earnings', 
                             'CAPE', 'TR CAPE', 'Excess CAPE Yield', 'Monthly Total Bond Returns', 
                             'Real Total Bond Returns', '10 Years Annualized Stock Real Return', 
                             '10 Years Annualized Bonds Real Return', 'Real 10 Years excess Annualized Returns'
                          ]
# Convert columns 2 to 20 to numeric and the Date column to string

data_shiller.iloc[:, 1:20] = data_shiller.iloc[:, 1:20].apply(pd.to_numeric, errors='coerce')
data_shiller['Date'] = data_shiller['Date'].astype(str)

# Drop rows where Date is NA
data_shiller = data_shiller.dropna(subset=['Date'])
# there is also a 'nan' in there, which appears different from NaN
data_shiller = data_shiller[data_shiller['Date'] != 'nan']

# Extract year and month from the Date, then form a new Date format
year = data_shiller['Date'].str.slice(0, 4)
month = data_shiller['Date'].str.slice(5, 7)
date = year + "-" + month + "-01"
data_shiller['Date'] = pd.to_datetime(date, errors='coerce')

#data_shiller['Date', 'S&P Comp', 'Dividend', 'Earnings', 
#  'Consumer Price CPI', 'Real price', 'Real Dividend', 
#  'Real Total Return Price', 'Real Earnings', 
#  'CAPE', '10 Years Annualized Stock Real Return', 
#  ].head()

# how to turn that type into e.g. JSON?  Or break it apart and return single
# >>> C= data_shiller[len(data_shiller)-1:]['CAPE']
# >>> C
# 1839    34.413463
# Name: CAPE, dtype: object
# 
## type conversion, then extraction
# >>> C.to_numpy()[0]
# 34.41346281338742

# CAPE
C = data_shiller[len(data_shiller)-1:]['CAPE']
print( C.to_numpy()[0] )
# Cyclically Adjusted Earnings
print (1 / C.to_numpy()[0])

# DATE OF CAPE
C = data_shiller[len(data_shiller)-1:]['Date']
TD = C.to_numpy()[0] 
TD = pd.to_datetime(TD)		# stinky conversion
print( TD.strftime("%Y-%m-%d") )

