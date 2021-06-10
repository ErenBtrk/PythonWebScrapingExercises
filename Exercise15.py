'''
15. Write a Python program to get the number of Pinterest accounts
maintained by U.S. State Department embassies and missions.
Source: https://www.state.gov/r/pa/ode/socialmedia/

'''

import requests
from lxml import html
url = 'http://www.state.gov/r/pa/ode/socialmedia/'
doc = html.fromstring(requests.get(url).text)
pinlinks = [a for a in doc.cssselect('a') if 'pinterest.com' in str(a.attrib.get('href'))]
print("The number of Pinterest accounts maintained by U.S. State Department embassies and missions:")
print(len(pinlinks))

iglinks = [a for a in doc.cssselect('a') if 'instagram.com' in str(a.attrib.get('href'))]
print("The number of Instragram accounts maintained by U.S. State Department embassies and missions:")
print(len(iglinks))
for item in iglinks:
    print(item.get("href"))