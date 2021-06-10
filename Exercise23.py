'''
23. Write a Python program to download IMDB's Top 250 data 
(movie name, Initial release, director name and stars).

'''

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url).text
soup = BeautifulSoup(response,"html.parser")

result = soup.find("tbody",{"class" : "lister-list"}).find_all("tr",limit=10)
print(result)

count = 0
for tr in result:
    title = tr.find("td",{"class" : "titleColumn"}).find("a").text
    year = tr.find("td",{"class" : "titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class" : "ratingColumn imdbRating"}).find("strong").text
    count += 1

    print(f"{count} . Movie : {title.ljust(60)}  Year = {year}  Rating = {rating}")

