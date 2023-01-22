import requests
from bs4 import BeautifulSoup

letters = 'abcdefghijklmnopqrstuvwxyz'
print('player_list = {')

for character in letters:
    weburl = f'https://www.basketball-reference.com/players/{character}/'
    page = requests.get(weburl)
    locateB = BeautifulSoup(page.content, 'html.parser')
    outcome = locateB.find(id='players')
    currentPlaying = outcome.find_all('tr')
    for player in currentPlaying[1:]:
        nbaName = player.find(attrs={'data-stat':'player'}).text.lower()
        year_max = player.find(attrs={'data-stat':'year_max'}).text
        if int(year_max) == 2022:
            print(f'\t"{nbaName}": ["{nbaName}", "{nbaName.split(" ")[-1]}"],')
print('}')