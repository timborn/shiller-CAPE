Thu Apr 25 10:36:36 MST 2024
----------------------------
We should be able to pull (and cache) current Cyclically Adjusted
Price Earnings ratio and also calculate Cyclically Adjusted Earnings
Yield (=1/CAPE).

The earnings yield turns out to be a reasonable predictor for real stock 
market returns over time periods >=10 years.

The Shiller CAPE data used to be on yale.edu website, but when I went 
looking I found stale data six months out.

Found what appears to be current data at https://shillerdata.com/
The link is labeled ie_data(xls).  Based on that "ver=xxx" it may also 
change over time, so extracting this programmatically may be interesting.
https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/ie_data.xls?ver=1712069253887

For now just download latest data by hand, as the code expects to find
ie_data.xls in the current directory.

If you just want to look at the graph:
https://ycharts.com/indicators/sandp_500_shiller_cape_earnings_yield
NB this also includes some basic analysis:
"S&P 500 Shiller Cyclically Adjusted Earnings Yield is at 2.91%,
compared to 2.94% last month and 3.48% last year. This is lower
than the long term average of 6.81%."

Combine this with the 10 year TIPS yield to get Excess Cape Yield.
This is the difference between inflation-adjusted Treasury yields
and the cyclically adjusted earnings yield.  Supposedly Shiller prefers
this to CAPE these days.  And it seems to be a metric in The Missing
Billionaires.

See Also
========
"Can The CAPE Ratio Predict Stock Market Returns?", 
https://www.quantifiedstrategies.com/can-the-cape-ratio-predict-stock-market-returns/  
Check out the regression graphs for 1,5,10 years



Getting Started
===============

### one-off crap to create an env in git
#? python3 -m venv --prompt "pyenv> " env
#? git init
#? echo 'env' > .gitignore	# the env folder we just created is not in git

### clean start, new machine
git clone repo
pip install -r requirements.txt	# install all needed pkgs

### typical usage pattern
source env/bin/activate	# to start using the environment
pip install <pkg>	# done while inside env
pip freeze > requirements.txt	# top level, above env!
deactivate		# to stop  using the environment

