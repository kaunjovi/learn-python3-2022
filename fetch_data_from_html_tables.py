import pandas as pd 

# html = "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes"
# html = "https://www.screener.in/company/HDFCBANK/consolidated/#balance-sheet"

# No tables here. Sorry. 
# html = "https://www.tickertape.in/stocks/hdfc-bank-HDBK/forecasts?checklist=basic&section=price"

# Pandas read_html() function is a quick and convenient way for scraping data from HTML tables.
# This function will always return a list of DataFrame or it will fail, e.g., it will not return an empty list.
tables = pd.read_html(html)

# How many tables did we find ? 
print(f"We found {len(tables)} tables in the HTML page.")

# Lets print the contents of the first table. 
print(f"{tables[4]}")
# display( simpsons[1].to_string())
# print(simpsons[0])

## Reference 
# Automate with Python – Full Course for Beginners - https://www.youtube.com/watch?v=PXMJ6FS7llk

