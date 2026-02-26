

from bs4 import BeautifulSoup
import requests
import pandas as pd

all_books = []

for page_num in range (1, 51):
  url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'lxml')
  books = soup.find_all('article', class_ = 'product_pod')
  for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_ = 'price_color').text.strip()
    all_books.append([title, price])

df = pd.DataFrame(all_books, columns = ['Title', 'Price'])

print(df)

df['Price'] = df['Price'].str.replace('Â', '')

print(df)

# df.to_csv('BookScraping.csv')

