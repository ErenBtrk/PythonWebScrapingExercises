'''
14. Write a Python program get the number of security alerts issued
by US-CERT in the current year.
Source: https://www.us-cert.gov/ncas/alerts

'''

#https://bit.ly/2lVhlLX
import requests
from lxml import html
url = 'https://us-cert.cisa.gov/ncas/alerts/2021'
doc = html.fromstring(requests.get(url).text)
print("The number of security alerts issued by US-CERT in the current year:")
print(len(doc.cssselect('.item-list li')))

for item in doc.cssselect('.item-list li div span a'):
    print(item.text)
