#!/usr/bin/env python3
# Bring back top search results in Google.
# From Automate the boring stuff.

import requests
import bs4
import webbrowser

searchfor = input("What would you like to search for?: ")
print("Googling....")  # Displays text while searching.
res = requests.get('http://google.com/search?q=%s' % searchfor)
res.raise_for_status()

# Retrieving top search results links.
soup = bs4.BeautifulSoup(res.text)

# Open the browser tab for each result.
linkElms = soup.select('.r a')
numOpen = min(3, len(linkElms))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElms[i].get('href'))
