import requests, json, os
from bs4 import BeautifulSoup

html = requests.get("http://www.kanjidamage.com/kanji").content
soup = BeautifulSoup(html)

kanji_table = soup.select(".table a")

kanjis = [{k.text:"http://www.kanjidamage.com/" + k.get("href")} for k in kanji_table]

"""
#for k in kanjis:
	#print(k)

with open("KanjiDamage.json", "w") as f:
	KD_json = json.dump(kanjis, f, ensure_ascii=False)
"""

# TODO: GET THIS TO WORK
with open("ib kanji.json", "r") as f:
	IB_Json = json.load(f)

	for k,v in IB_Json.items():
		for ki in kanjis:
			print(ki)

IB_And_KanjiDamage = []