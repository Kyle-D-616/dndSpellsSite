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
    #spell name
    spellDiv = soup.find('div', {'class': 'page-title page-header'})
    spellName = spellDiv.find('span').get_text(strip=True)

    #spell body
    spellBodyDiv = soup.find('div', {'id': 'page-content'})
    spellBody = spellBodyDiv.find_all('p')
    attributes={f'atr{i+1}': p.get_text(strip=True) for i, p in enumerate(spellBody)}

    print(attributes)
