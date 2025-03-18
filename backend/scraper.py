import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.chrono24.com/rolex/index.html"

def scrape_data():
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = []
    for item in soup.select('.article-item-container'):
        try:
            model = item.select_one('.text-ellipses').text.strip()
            price = item.select_one('.price').text.strip()
            year = item.select_one('.year').text.strip()
            condition = item.select_one('.condition').text.strip()
            listings.append({
                'model': model, 
                'price': int(price), 
                'year': year, 
                'condition': condition
            })
        except:
            continue

    df = pd.DataFrame(listings)
    print('Scraped: ')
    print(df.head())
    df.to_csv('rolex_prices.csv', index = False)
    print('Scraping complete. Rolex listings saved as rolex_prices.csv')

if __name__ == '__main__':
    scrape_data()


