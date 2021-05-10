import requests
import json
import sys
import subprocess
import urllib.request
import os

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
    print_image(size=1)
    # lp = subprocess.Popen([
    #     "/usr/bin/lp", "-o", "PageSize=X72MMY50MM", "-o", "PrintSpeed=2Low", "-o", "landscape", "-d", "PDF", "token.jpg"])


def print_image(size=0):
    argslist = [
        "/usr/bin/lp", "-o", "PrintSpeed=2Low"]

    if 'print_device' in os.environ and os.environ['print_device'] == 'PDF':
        print("running a test")
        argslist.append("-d")
        argslist.append("PDF")
    else:
        print("oops")

    if size == 0:
        argslist.append("-o")
        argslist.append("PageSize=X72MMY50MM")
        argslist.append("-o")
        argslist.append("landscape")

    if size == 1:
        argslist.append("-o")
        argslist.append("PageSize=X72MMY50MM")
        argslist.append("-o")
        argslist.append("portrait")
        argslist.append("-o")
        argslist.append("scaling=85")

    else if size == 2:
        argslist.append("-o")
        argslist.append("PageSize=X72MMY100MM")
        argslist.append("-o")
        argslist.append("portrait")

    argslist.append("token.jpg")
    lp = subprocess.Popen(argslist)
