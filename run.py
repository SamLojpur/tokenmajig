import requests
import json
import sys
import subprocess
import urllib.request

card = requests.get(
    'https://api.scryfall.com/cards/named?fuzzy=Wasitora').json()
print("Ok")
for token in [card_part for card_part in card['all_parts'] if card_part['component'] == 'token']:
    token_image = requests.get(token['uri']).json()[
        'image_uris']['border_crop']
    print(token_image)
    urllib.request.urlretrieve(
        token_image, "token.jpg")
    # lp = subprocess.Popen([
    #     "/usr/bin/lp", "-o", "PageSize=X72MMY100MM", "-o", "PrintSpeed=2Low", "-o", "portrait", "-d", "PDF", "token.jpg"])
    lp = subprocess.Popen([
        "/usr/bin/lp", "-o", "PageSize=X72MMY50MM", "-o", "PrintSpeed=2Low", "-o", "landscape", "-d", "PDF", "token.jpg"])
