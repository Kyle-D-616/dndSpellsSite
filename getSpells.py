from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()

url = 'https://dnd5e.wikidot.com/spells'

urlResponse = session.get(url)

soup = BeautifulSoup(urlResponse.content, 'html.parser')
table = soup.find('table')
rows = soup.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    print(row_data)


print(table)
#products = r.html.find('')


