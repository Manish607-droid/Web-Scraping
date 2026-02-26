from bs4 import BeautifulSoup
import requests
import pandas as pd

all_data = []



for page_number in range(1,25):
  url = f'https://www.scrapethissite.com/pages/forms/?page_num={page_number}'
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'lxml')
  if page_number == 1:
    table = soup.find_all('th')
    hockey_table = [title.text.strip() for title in table]
  team_data = soup.find_all('tr')

  for row in team_data[1:]:
    row_data = row.find_all('td')
    team_row_data = [data.text.strip() for data in row_data]
    all_data.append(team_row_data)
df = pd.DataFrame(all_data, columns = hockey_table)

df.to_csv('hockeyconvert.csv')