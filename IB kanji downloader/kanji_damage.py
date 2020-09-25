import requests, json, os
from bs4 import BeautifulSoup

"""
html = requests.get("http://www.kanjidamage.com/kanji").content
soup = BeautifulSoup(html)

kanji_table = soup.select(".table a")

kanjis = [{k.text:"http://www.kanjidamage.com/" + k.get("href")} for k in kanji_table]


#for k in kanjis:
	#print(k)

with open("KanjiDamage.json", "w") as f:
	KD_json = json.dump(kanjis, f, ensure_ascii=False)
"""

# TODO: GET THIS TO WORK
with open("ib kanji.json", "r") as f:
	IB_Json = json.load(f)

with open("KanjiDamage.json", "r") as kdf:
	KD_JSON = json.load(kdf)

"""
# HL 600 IB
HL_Kanji = set(IB_Json.get("HL_Kanji"))
KD_Kanji = set([k for d in KD_JSON for k in d])

HL_IB_AND_KD = list(KD_Kanji.intersection(HL_Kanji))


HL_IB_AND_KD_JSON = [{kanji:link} for kd_dict in KD_JSON for kanji, link in kd_dict.items() if kanji in HL_Kanji]
print(len(HL_IB_AND_KD_JSON),HL_IB_AND_KD_JSON)

#print(len(HL_IB_AND_KD), HL_IB_AND_KD)
"""
def write2JSON(ibjson):
	HL_Kanji = set(ibjson)
	KD_Kanji = set([k for d in KD_JSON for k in d])

	HL_IB_AND_KD = list(KD_Kanji.intersection(HL_Kanji))

	return [{kanji:link} for kd_dict in KD_JSON for kanji, link in kd_dict.items() if kanji in HL_Kanji]

SL_IB_AND_KD_JSON = write2JSON(IB_Json.get("SL_Kanji"))
HL_IB_AND_KD_JSON = write2JSON(IB_Json.get("HL_Kanji"))
HL_EXTRA_IB_AND_KD_JSON = write2JSON(IB_Json.get("HL_Extra_Kanji"))

JSON_DICT = {"SL_IB_AND_KD_JSON":SL_IB_AND_KD_JSON, "HL_IB_AND_KD_JSON":HL_IB_AND_KD_JSON, "HL_EXTRA_IB_AND_KD_JSON":HL_EXTRA_IB_AND_KD_JSON }

with open("KanjiDamageIBKanji.json", "wb")as f:
    f.write(json.dumps(JSON_DICT, ensure_ascii=False, indent=4).encode("utf-8"))

