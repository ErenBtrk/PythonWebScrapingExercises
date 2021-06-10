'''
8. Write a Python program to extract and display all the image links
from en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer). 
 
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)"
html = urlopen(url)
soup = BeautifulSoup(html,"html.parser")

result = soup.find_all("img",{'src':re.compile('.jpg')})

for image in result: 
    print(image['src']+'\n')