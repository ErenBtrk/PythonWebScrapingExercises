'''
25. Write a Python program to get the number of magnitude
4.5+ earthquakes detected worldwide by the USGS.
 
'''

import csv
import requests
csvurl = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv'
rows = list(csv.DictReader(requests.get(csvurl).text.splitlines()))
print("The number of magnitude 4.5+ earthquakes detected worldwide by the USGS:", len(rows))
  