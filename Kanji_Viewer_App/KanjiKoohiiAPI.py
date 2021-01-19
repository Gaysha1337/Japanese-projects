
import json, requests, random, concurrent.futures, re
from typing import OrderedDict
from os import sep
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession, AsyncHTMLSession
from multiprocessing import Pool
import ankipandas

def stories_csv_to_json():
    with open("ib kanji.json", "r",encoding="utf-8")as f:
        data = json.load(f)
        HL_kanji = data.get("HL_Kanji")

    csv_file = pd.DataFrame(pd.read_csv("my_stories.csv", sep = ",", index_col=False))
    csv_file = csv_file.drop(["public", "last_edited"],axis=1)

    koohii_kanji = {k[0] for k in csv_file[["kanji"]].values}
    HL_kanji = set(HL_kanji)
    #csv_file.to_json("my_stories_json.json")

    HL_kanji_intersection = HL_kanji.intersection(koohii_kanji)

    # Kanji that are in the "ib kanji.json" but not in "my_stories.csv"
    # Stories need to be extracted from the site
    HL_kanji_difference = HL_kanji.difference(koohii_kanji)
    print(len(HL_kanji_difference))
    return sorted(HL_kanji_difference)


paired_slicer = lambda arr,n: (arr[i:i+n] for i in range(0,len(arr),n))


koohii_data, error_kanji = [], []
def get_koohii_from_ib_kanji_json(kanji):
    # List or signle kanji string
    #print(type(kanji))    

    login_url = "https://kanji.koohii.com/login"

    data = {"username": "Gaysha1337","password": "GloriousPC1337"}

    headers = {
        #"cookie": "koohii=n2k194rot7u4or8og9fgmstk62",
        'Connection': 'Keep-Alive',
        "dnt": "1",
        'Keep-Alive': 'timeout=0, max=500',
        "origin": "https://kanji.koohii.com",
        #"referer": "https://kanji.koohii.com/account",
        "sec-ch-ua": "'Google Chrome';v='87', 'Not;A Brand';v='99', 'Chromium';v='87'",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    """
    with requests.Session() as s:
        koohii_data = []
        for i, k in enumerate(set(kanji)):
            s.post(login_url, headers=headers, data=data)
            search_url = f"https://kanji.koohii.com/study/kanji/{k}"
            _headers = {
                #"cookie": "koohii=n2k194rot7u4or8og9fgmstk62",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            r = s.get(search_url, headers=_headers,  timeout=None)
            if r.ok:
                soup = BeautifulSoup(r.content, features="lxml")
                print(i,":",k)
                framenr  = soup.select_one("div.framenum").text.strip()
                keyword = soup.select_one("div.keyword").text.strip()
                story = soup.select_one("#storyview").text.strip().replace('"',"'")

                if story == "[ click here to enter your story ]": story = [s.text.strip().replace('"',"'") for s in soup.select(".story")]
                koohii_data.append({"framenr":framenr,"kanji":k,"keyword":keyword,"story":story})
        #return koohii_data
        with open("kanji_koohii.json","wb") as f:
            f.write(json.dumps(koohii_data, ensure_ascii=False, indent=4).encode("utf-8"))
    """

    with HTMLSession() as s:
        
        for i, k in enumerate(set(kanji)):

            """
            for kk_dict in kanji_koohii_json:
                if k == kk_dict.get(k):
                    print(k, "in json") 
                    continue
                else: print(f"{k} not in json")
            """
            request_status = None
            
            initial_request = s.post(login_url, headers=headers, data=data)
            search_url = f"https://kanji.koohii.com/study/kanji/{k}"
            _headers = {
                #"cookie": "koohii=n2k194rot7u4or8og9fgmstk62",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            r = s.get(search_url, headers=_headers, timeout=None)
                

            #soup = BeautifulSoup(r.content, features="lxml")
            #print(initial_request.headers)
            
            soup = r.html
            #print(i,":",k)
            #print(r.content)
            
            framenr  = soup.find("div.framenum", first=True)
            keyword = soup.find("div.keyword", first=True)
            story = soup.find("#storyview",first=True)

            if story == "[ click here to enter your story ]": story = [s.text.strip().replace('"',"'") for s in soup.find(".story")]
            #koohii_data.append({"framenr":framenr,"kanji":k,"keyword":keyword,"story":story})
            #koohii_data.append({"framenr":framenr,"kanji":k,"keyword":keyword,"story":story})
            try:
                kanji_dict = OrderedDict([("framenr",framenr.text.strip()),("kanji",k),
                    ("keyword",keyword.text.strip()),("story",story.text.strip().replace('"',"'"))])
                koohii_data.append(kanji_dict)
                if len(koohii_data) == 1: return dict(kanji_dict)
                #print(koohii_data)
            except: 
                #r.raise_for_status()
                error_kanji.append([k,i])
                print(f"Added {k} to error array")
                print("Error Array", error_kanji, "koohii arr", koohii_data, sep="\n")
                with open("Error Kanji.txt","a+", encoding="utf-8") as f:
                    f.write(f"{k}:{i}")

            
                if koohii_data:
                    with open("kanji_koohii.json","ab+") as f:
                        f.write(json.dumps(koohii_data, ensure_ascii=False, indent=4).encode("utf-8"))
            

        return koohii_data
        

if __name__ == "__main__":
    anki_filename, notes_filename = "Anki Remembering the Kanji.txt", "Notes Anki Remembering the Kanji.txt"
    anki_json = "deck.json"

    anki_col_path = "Remembering the Kanji.apkg"

    pd.set_option('display.max_colwidth', None)
    col = ankipandas.Collection()#"C:\Users\dimit\AppData\Roaming\Anki2\User 1\collection.anki2")
    print(col.cards.fields_as_columns(inplace=True))

    with open(anki_json, "r", encoding="utf-8") as f:
        """
        for i, l in enumerate(f.readlines()[1:]):
            #print(l.strip())
            #if i == 0: break
            #pattern = ".*Details Story Dictionary (\D)(.*)My Story (.*)Koohii(.*#\d).*(Primitives.*)(Kunyomi:.*)(Onyomi:.*)(Lesson:.*)(JH JLPT Level:.*)(Compounds:.*?)"
            pattern = ".*Details Story Dictionary (\D)(.*)My Story (.*)Koohii(.*#\d).*(Primitives.*)(Kunyomi:.*)(Onyomi:.*)(Lesson:.*)(JH JLPT Level:.*)(Compounds:.*)"
            if i == 1:
                #print(l)
                regex = re.compile(pattern)
                #print("\n\n",re.findall(regex, l)) 
                break
        """    
        pass
        
        
        #pd.set_option("max_columns", None) # show all cols
        #pd.set_option('max_colwidth', None) # show full width of showing cols
        #pd.set_option("expand_frame_repr", False) # print cols side by side as it's supposed to be 
        #df = pd.read_fwf(f, delimit_whitespace=True, skipinitialspace=True, encoding="utf-8", header=None).apply(lambda x: x.str.strip() if x.dtype == "object" else x)#.applymap(lambda x: x.strip() if type(x)==str else x)
        #df = pd.read_json(f)
        #df = pd.read_csv(f, sep="\t", header=None)#.apply(lambda x: str(x).strip())
        #df = df.iloc[0]
        
        #pd.DataFrame().iloc[[0]]
        #print(df.iloc[[2][0]])
        #print(df)
    #df.to_csv('log.csv') 
    """
    arr = ["客", "朝","朝","船","観","的","客","室"]

    kanji_arr = stories_csv_to_json()

    for i,sublist in enumerate(paired_slicer(kanji_arr,4)):
        print("sublist", sublist)
        get_koohii_from_ib_kanji_json(sublist)

    if koohii_data:
        with open("kanji_koohii.json","wb") as f:
            print("writing to file")
            f.write(json.dumps(koohii_data, ensure_ascii=False, indent=4).encode("utf-8"))

    
    #print(get_koohii_from_ib_kanji_json(arr[0:3]))
    #print(stories_csv_to_json())
    """

    
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(get_koohii_from_ib_kanji_json, kanji=kanji) for kanji in stories_csv_to_json()]
        
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    #get_koohii_from_ib_kanji_json(stories_csv_to_json())
    """