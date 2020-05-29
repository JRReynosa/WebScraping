#! python3
# searchpypi.py  - Opens several search results.

import sys
# Added line below to fix the 'bs4 moduel not found error'
sys.path.append(r'C:\Users\reynosaj\PycharmProjects\WebScraping\venv\Lib\site-packages')

import pyperclip
import requests
import webbrowser
import bs4


print('Searching...')  # display text while downloading the search result page

# If arguments entered, then get argument
if len(sys.argv) > 1:
    arg = ' '.join(sys.argv[1:])
# Else copy from clipboard
else:
    arg = pyperclip.paste()

# Make request to page
url = 'https://pypi.org/search/?q=' + arg
res = requests.get(url)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
