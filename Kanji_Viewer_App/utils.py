import json, requests, random, sys, os
from bs4 import BeautifulSoup

# Kivy
from kivymd.app import MDApp
from kivymd.toast import toast
    
 
def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

""" Screen Methods"""

def create_screen(name, content, *args, **kwargs):
    from KanjiScreen import GeneralScreen
    screen = GeneralScreen(name=name)
    screen.add_widget(content)
    MDApp.get_running_app().screen_manager.add_widget(screen)

def switch_to_screen(screen_name):
    master = MDApp.get_running_app()
    master.screen_manager.current = screen_name
    master.current_screen = master.screen_manager.get_screen(master.screen_manager.current)
    
    #print(MDApp.get_running_app().current_screen.name, "switch method")

# Kill and reload a screen to show any GUI changes
def kill_screen(screen_name, reload_func, *args):
    master = MDApp.get_running_app()
    if master.screen_manager.has_screen(screen_name):
        master.screen_manager.clear_widgets(screens=[master.screen_manager.get_screen(screen_name)])
    reload_func()
    switch_to_screen(screen_name)

def get_kanji_data(kanji):
    # 家庭
    url = f"https://www.japandict.com/kanji/{kanji}?lang=en"
    with requests.Session() as s:
        try:
            r = s.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"})
            soup = BeautifulSoup(r.content, features="lxml")
            stroke_imgs = ["https://www.japandict.com" + img.get("src")for img in soup.select("li.list-group-item img")]
            stroke_count = soup.find(lambda tag:tag.name=="li" and "Number of strokes:" in tag.text).text.strip()

            #readings = [i.text.replace("yomi","yomi: ") for i in soup.select(".m-b-0") if "Nanori" not in i.text.strip()]
            english_meanings = [m.text.strip() for m in soup.select(".bordered-tab-contents .list-group-item:first-child", text=True)][0]

            radicals_text = [radical.text.strip() for radical in soup.select("ul.list-group.list-group-flush h3")]
            radicals_meaning = [radical.text.strip() for radical in soup.select("ul.list-group.list-group-flush p") if not radical.has_attr("class")]

            #word_examples_kanji = [word for word in soup.select("ul.list-group a") if "/kanji" not in word.attrs.get("href")] # if word.name in ("a","p","span","h4")
            #word_examples_kanji = list(filter(lambda i: i[0] is not None,[[word.select_one("h4"), word.select_one("span"), word.select_one("p")] for word in soup.select("ul.list-group a")])) # if word.name in ("a","p","span","h4")
            word_examples_kanji = [f"{word.select_one('h4').text.strip()} ({word.select_one('span').text.strip()}) : {word.select_one('p').text.strip()}" for word in soup.select("ul.list-group a") if word.select_one("h4") is not None] # if word.name in ("a","p","span","h4")
            readings_dict = {}
            
            for i in soup.select(".list-group-item .m-b-0"):
                if "Nanori" in i.text: 
                    continue
                if "On'yomi" in i.text:
                    readings_dict["On'yomi"] = " ".join([p.text + " ," for r in i for p in r if not isinstance(p, str)])
                if "Kun'yomi" in i.text:
                    readings_dict["Kun'yomi"] = " ".join([p.text + " ," for r in i for p in r if not isinstance(p, str)])
            
            print("Radicals: ", list(zip(radicals_text, radicals_meaning)))
            
            return  {
                "kanji":kanji,
                "readings":readings_dict,
                "meanings":english_meanings,
                "stroke_count":stroke_count.replace("Number of strokes: ","") + " Strokes",
                "stroke_order_images":stroke_imgs,
                "radicals_data":list(zip(radicals_text, radicals_meaning)),
                "example_words": word_examples_kanji
            }
    
        except Exception as e:
            print(e)
            return {}
    
            
def get_kanji_from_level(level):
    level = level.strip().replace(" ","_")
    with open(resource_path("DATA/ib kanji.json"),"r", encoding="utf-8") as f:
        data = json.load(f)
        return get_kanji_data(random.choice(data.get(level))) or None

if __name__ == "__main__":
    k = "晩" #"数"
    k = "等"
    get_kanji_data(k)
    #print(get_kanji_data(k))
    #get_kanji_from_level("SL Kanji")