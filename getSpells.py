from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()

baseUrl = 'https://dnd5e.wikidot.com/spells'
spellUrl = f'https://dnd5e.wikidot.com{}'


urlResponse = session.get(baseUrl)
spellsUrlResponse = session.get(?)

soup = BeautifulSoup(urlResponse.content, 'html.parser')
table = soup.find('div', {'class': 'yui-content'})
spellUrls = []
for url in table.find_all('a'):
    spellUrls.append('https://dnd5e.wikidot.com'+url.get('href'))
print(spellSoup)
