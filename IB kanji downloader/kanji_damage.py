import requests, json
from bs4 import BeautifulSoup

html = requests.get("http://www.kanjidamage.com/kanji").content
soup = BeautifulSoup(html)

kanji_table = soup.select(".table a")

kanjis = [{k.text:"http://www.kanjidamage.com/" + k.get("href")} for k in kanji_table]
for k in kanjis:
	print(k)