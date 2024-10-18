import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target url to scrape
url = "https://en.wikipedia.org/wiki/FTSE_250_Index#Constituents"

# Get request the page
response = requests.get(url)

# Parse contents of page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tables on page
tables = soup.find_all('table', class_='wikitable')

# Check for third table (FTSE 250 companies)
if len(tables) >= 3:
    # Choose third table
    table = tables[2]
    # store data from table in list
    data = []

    # Extract data row at a time for company, ticker, and industry
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) > 1:
            # Extract data
            company = cols[0].text.strip()
            ticker = cols[1].text.strip()
            industry = cols[2].text.strip()

            # Append row data to the list
            data.append({
                'Company': company,
                'Ticker': ticker,
                'Industry': industry
            })

    # Make it a dataframe to export
    df = pd.DataFrame(data)

    df.to_csv('FTSE_250_SCRAPE.csv', index=False)
else:
    print("There is no third table on this page")
