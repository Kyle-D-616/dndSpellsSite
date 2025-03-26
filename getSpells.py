from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()

url = 'https://dnd5e.wikidot.com/spells'

urlResponse = session.get(url)

soup = BeautifulSoup(urlResponse.content, 'html.parser')
table = soup.find('div', {'class': 'yui-content'})
urls = []
for url in table.find_all('a'):
    urls.append(url.get('href'))
print(urls)
