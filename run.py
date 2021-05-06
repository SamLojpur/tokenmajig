import requests
import json
import sys
import subprocess

card = requests.get(
    'https://api.scryfall.com/cards/named?fuzzy=outlaws+merriment').json()
print("Ok")
for token in [card_part for card_part in card['all_parts'] if card_part['component'] == 'token']:
    token_image = requests.get(token['uri']).json()[
        'image_uris']['border_crop']
    print(token_image)
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
lpr.stdin.write(your_data_here)
# uri = token['uri']
# print(r.json())
