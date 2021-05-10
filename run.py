import requests
import json
import sys
import subprocess
import urllib.request
import os


def print_uri(uri, size=0):
    print(uri)
    urllib.request.urlretrieve(
        uri, "token.jpg")

    argslist = [
        "/usr/bin/lp", "-o", "PrintSpeed=2Low"]

    if 'print_device' in os.environ and os.environ['print_device'] == 'PDF':
        print("Printing as PDF instead")
        argslist.append("-d")
        argslist.append("PDF")

    if size == 's':
        argslist.append("-o")
        argslist.append("PageSize=X72MMY50MM")
        argslist.append("-o")
        argslist.append("landscape")

    elif size == 'm':
        argslist.append("-o")
        argslist.append("PageSize=X72MMY100MM")
        argslist.append("-o")
        argslist.append("portrait")
        argslist.append("-o")
        argslist.append("scaling=90")

    elif size == 'l':
        argslist.append("-o")
        argslist.append("PageSize=X72MMY100MM")
        argslist.append("-o")
        argslist.append("portrait")

    else:
        print("unknown size")

    argslist.append("token.jpg")
    lp = subprocess.Popen(argslist)


while True:
    print("Input command and query:")

    input_raw = input()

    input_split = input_raw.split(' ')
    code = input_split[0]
    del input_split[0]
    if not (code == 't' or code == 'c' or code == 'm'):
        print("error: unknown action code")

    query = []
    size = 'm'

    input_split.reverse()

    for i, input_token in enumerate(input_split):
        if input_token == '-s':
            size = input_split[i-1]
            query.pop()
        else:
            query.append(input_token)
    query.reverse()
    query = "+".join(query)

    if code == "c":
        card = requests.get(
            'https://api.scryfall.com/cards/named?fuzzy=' + query).json()
        card_image = card['image_uris']['border_crop']
        print_uri(card_image, size=size)

    elif code == "t":
        card = requests.get(
            'https://api.scryfall.com/cards/named?fuzzy=' + query).json()
        for token in [card_part for card_part in card['all_parts'] if card_part['component'] == 'token']:
            token_image = requests.get(token['uri']).json()[
                'image_uris']['border_crop']
        print_uri(token_image, size=size)

    elif code == "m":
        card = requests.get(
            'https://api.scryfall.com/cards/random?q=t:creature+not:funny+cmc:' + query).json()
        card_image = card['image_uris']['border_crop']
        print_uri(card_image, size=size)
