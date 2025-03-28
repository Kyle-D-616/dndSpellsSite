from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()

baseUrl = 'https://dnd5e.wikidot.com/spells'
#spellUrl = f'https://dnd5e.wikidot.com{}'


urlResponse = session.get(baseUrl)

soup = BeautifulSoup(urlResponse.content, 'html.parser')
table = soup.find('div', {'class': 'yui-content'})
spellUrls = []
for url in table.find_all('a'):
    spellUrls.append('https://dnd5e.wikidot.com'+url.get('href'))

spells = []
for spellUrl in spellUrls:
    urlResponse = session.get(spellUrl)
    soup = BeautifulSoup(urlResponse.content, 'html.parser')
    spell = soup.find('div', {'class': 'page-title page-header'})
    print(spell)
    '''spellInfo = soup.find('div', {'class': 'page-content'})
    spells.append({spell.get('span'): spellInfo.text} )'''
