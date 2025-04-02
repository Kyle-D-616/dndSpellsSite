
from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()

baseUrl = 'https://dnd5e.wikidot.com/spells'

urlResponse = session.get(baseUrl)

soup = BeautifulSoup(urlResponse.content, 'html.parser')
table = soup.find('div', {'class': 'yui-content'})
spellUrls = []
for url in table.find_all('a'):
    spellUrls.append('https://dnd5e.wikidot.com' + url.get('href'))

spells = []
for spellUrl in spellUrls:
    urlResponse = session.get(spellUrl)
    soup = BeautifulSoup(urlResponse.content, 'html.parser')

    # Spell name
    spellDiv = soup.find('div', {'class': 'page-title page-header'})
    spellName = spellDiv.find('span').get_text(strip=True)

    # Spell body
    spellBodyDiv = soup.find('div', {'id': 'page-content'})
    spellBody = spellBodyDiv.find_all(['p', 'ul'])  # Now include <ul> elements

    attributes = {}
    attr_index = 1

    # Process each element in spell body
    for p in spellBody:
        if p.name == 'p':  # If it's a <p> tag, process it as a paragraph
            # Replace <br> tags with a unique placeholder
            for br in p.find_all('br'):
                br.replace_with('|')  

            # Split text by the placeholder
            parts = p.get_text(strip=True).split('|')

            # Save each part as an attribute
            for part in parts:
                attributes[f'atr{attr_index}'] = part.strip()
                attr_index += 1

        elif p.name == 'ul':  # If it's a <ul> tag, process list items
            list_items = p.find_all('li')
            for item in list_items:
                attributes[f'atr{attr_index}'] = item.get_text(strip=True)
                attr_index += 1

    # Append the spell data with its name and attributes
    spells.append({
        'name': spellName,
        'attributes': attributes
    })

# Print sample output
'''for spell in spells[-5:]:  # Print only the last 5 spells for preview
    print(f"Spell: {spell['name']}")
    for key, value in spell['attributes'].items():
        print(f"  {key}: {value}")
    print("-" * 50)'''

