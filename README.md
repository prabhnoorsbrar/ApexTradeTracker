TradeTracker.py ---- Driver script: Meant to scrape account balance and account threshold from apex trading website. 
DataInjector.py ---- meant to take input data from tradetracker and inject into local csv(s) (based on how many prop firm accounts you have)
CreateSheets.py ---- Takes in local data from CSV and then correctly updates/replaces csv data to google sheets data

DATA FROM APEXTRADERFUNDING.COM meant to be scraped at 3PM PST(6PM EST), this is when your daily account balance and threshold updates.
