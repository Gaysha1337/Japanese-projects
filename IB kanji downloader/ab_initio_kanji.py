import requests,json
from bs4 import BeautifulSoup

url="https://quizlet.com/202819846/japanese-ab-initio-kanji-flash-cards/"


#document.getElementsByClassName("TermTextnotranslatelang-ja")
if __name__=="__main__":
    
    x = """
    一
    二
    三
    四
    五
    六
    七
    八
    九
    十
    百
    千
    万
    円
    数
    曜
    日
    月
    火
    水
    木
    金
    土
    今
    時
    週
    年
    間
    毎
    半
    分
    午
    朝
    昼
    夜
    夕
    大
    小
    新
    高
    白
    黒
    赤
    青
    少
    多
    近
    古
    安
    好
    長
    強
    楽
    美
    早
    速
    静
    正
    寒
    暑
    遠
    広
    上
    下
    中
    前
    後
    外
    右
    左
    次
    先
    人
    女
    男
    子
    父
    母
    兄
    弟
    姉
    妹
    親
    友
    私
    口
    目
    山
    田
    川
    海
    電
    雨
    天
    気
    晴
    石
    見
    出
    入
    食
    飲
    聞
    行
    来
    話
    書
    買
    生
    会
    休
    有
    言
    住
    売
    知
    思
    帰
    教
    読
    作
    泳
    例
    乗
    通
    終
    始
    回
    続
    春
    夏
    秋
    冬
    北
    南
    東
    西
    方
    学
    校
    本
    語
    何
    名
    勉
    京
    都
    国
    地
    図
    島
    町
    駅
    店
    車
    道
    旅
    社
    所
    屋
    室
    家
    場
    公
    園
    同
    音
    全
    員
    様
    """.replace("\n", " ").replace(" ","").strip().split(",")
    print(len(list(",".join(x))), len(set(",".join(x))))
