import pandas as pd
import numpy as np
import sys

def usage():
  print("Error: mandatory command line choice:")
  print("  CAPE - if you want the CAPE number")
  print("  EARNINGS - Cyclically Adjusted Earnings")
  print("  CDATE - date of that CAPE number, to make sure it's fresh")
  exit(1)

# process mandatory command line option:
# $0 [CAPE|CDATE] 
if len(sys.argv) != 2:
  usage()

switcher = {
  "CAPE": "CAPE",
  "EARNINGS": "EARNINGS",
  "CDATE": "CDATE"
}
# quick check to make sure we have something we recognize
persona = switcher.get(sys.argv[1], "NOPE")
if (persona == "NOPE"): usage()

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

C = data_shiller[len(data_shiller)-1:]['CAPE']
if (persona == "CAPE"):
  print( C.to_numpy()[0] )

if (persona == "EARNINGS"):
  # Cyclically Adjusted Earnings
  print (1 / C.to_numpy()[0])

if (persona == "CDATE"):
  # DATE OF CAPE
  C = data_shiller[len(data_shiller)-1:]['Date']
  TD = C.to_numpy()[0] 
  TD = pd.to_datetime(TD)		# stinky conversion
  print( TD.strftime("%Y-%m-%d") )
  
