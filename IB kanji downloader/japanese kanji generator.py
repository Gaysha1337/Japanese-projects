import os
import tika
tika.initVM()
from tika import parser
kanji_pdf = parser.from_file("ib_kanji_list_for_2020.pdf")

print(kanji_pdf["content"])
print("here")