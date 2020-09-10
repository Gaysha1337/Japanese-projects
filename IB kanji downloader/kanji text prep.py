import json
import re

"""
with open("kanji copy.txt", "r", encoding="utf-8") as f:
    
    for l in f.readlines():
        #if l != "HLとSLの400字" or l != "HL only" :
        print(l.split(","))
    
    print(f.read().split(","))
"""
Kanji_original = [
'HLとSLの400字','—', '人', '二', '七', '八', '九', '十', '入', '山', '二','才', '川', '口', '土', '子', '女', '千', '万', '上', '下','大', '小', '日', '月', '木',
 '火', '水', '五', '六', '円','中', '手', '分', '文', '少', '午', '今', '友', 
 '父', '公','犬', '元', '天', '田', '広', '生', '立', '四', '本', '半','目', '石', '古', '母', '兄', '出', '右', '左', '北', '外','市', '白', '冬', '正', '号', '先', 
 '同', '州', '回', '全','次', '百', '年', '休', '好', '耳', '肉', '字', '安', '多','行', '毎', '会', '気', '有', '名', '早', '西', '地', '市','私', '図', '何', '男',
 '足', '花', '売', '近', '社', '來','見', '作', '言', '弟', '走', '住', '町', '村', '赤', '金','始', '例', '空', '泳', '知', '明', '学', '林', '雨', '物','長', '夜', 
 '英', '店', '国', '青', '姉', '妹', '歩', '東','所', '京', '茶', '美', '乗', '食', '昼', '前', '後', '海','室', '南', '思', '春', '秋', '点', '高', '島', '速','旅',
 '通', '帰', '書', '校', '時', '家', '勉', '夏', '魚', '都','終', '週', '静','閉', '強', '滞', '森', '暑', '寒', '番','病', '場', '間', '短', '飲', '買', '朝', '晚', 
 '飯', '開','道', '晴', '新', '鉄', '園', '数', '続', '暗', '話', '電','遠','楽', '聞', '様', '読', '語', '駅', '曜', '親', '薬','夕', '方', '切', '止', '内', '着', 
 '欠', '予', '心', '比','王', '反', '化', '世', '太', '引', '主', '力','必', '写','民', '台', '区', '平', '失', '牛', '以', '史', '去', '他','仕', '由','用', '法', 
 '式', '米', '危', '未', '昔', '忙','色', '当', 'ム', '寺', '蜜', '伝', '因', '成', '代', '両','死', '再', '在', '交', '自', '体', '位', '低', '助', '変','初', '君', 
 '完', '利', '返', '冷', '良', '決', '局', '忘','考', '対', '徒', '別', '門', '度', '各', '実', '医', '卒','的', '季', '彼', '若', '育', '使', '定','和', '事', '組',
 '者', '注', '服', '単', '発', '界', '待', '秒', '神', '昨','参','計', '客', '室', '持', '降', '県', '科', '映', '画','音', '送', '席', '洋', '活', '洗', '要', '品', 
 '便', '段','留', '展', '係', '重', '院', '庭', '配', '倍', '味', '酒','部', '料', '起', '借', '記', '員', '真', '紙', '蜜', '原','流', '動', '教', '転', '現', '族', 
 '第', '祭', '険', '習','問', '宿', '理', '遊', '悪', '特','遅', '経', '歌', '僕','絵', '給', '答', '貸', '温', '階', '勝', 'ハ', '最', '集','験', '慟', '授', '寝', 
 '費', '節', '漢', '業', '希', '意','感', '練', '橋', '歴', '説', '関', '望', '適', '銀', '館','調', '質', '題', '熱', '選', '顔', '願', '賛', '頭', '簡','々', '工', 
 '功', '夫', '不', '払', '礼', '可', '庁', '宅','件', '団', '向', '老', '争', '任', '汚', '困', '条', '判','風', '役', '労', '努', '均', '究', '投', '技', '身', '求',
 '出', '妻', '命', '招', '官', '府', '治','宗', '材', '存','表', '果', '受', '念', '非', '泊', '応', '取', '具', '性','価','泣', '並', '述', '保', '面', '示', '苦', 
 '飛', '省','直', '祝', '逆', '師',  '和', '事', '組','者', '注', '服', '単', '発', '界', '待', '秒', '神', '昨','参', '計', '客', '室', '持', '降', '県', '科', '映', 
 '画','音', '送', '席', '洋', '活', '洗', '要', '品', '便', '段','留', '展', '係', '重', '院', '庭', '配', '倍', '味', '酒','部', '料', '起', '借', '記', '員', '真', 
 '紙', '蜜', '原','流', '動', '教', '転', '現', '族', '第', '祭', '険', '習','問', '宿', '理', '遊', '悪', '特', '遅', '経', '歌', '僕','絵', '給', '答', '貸', '温', 
 '階', '勝', 'ハ', '最', '集','験', '慟', '授', '寝', '費', '節', '漢', '業', '希', '意','感', '練', '橋', '歴', '説', '関', '望', '適', '銀', '館','調', '質', '題', 
 '熱', '選', '顔', '願', '賛', '頭', '簡','HL only','々', '工', '功', '夫', '不', '払', '礼', '可', '庁', '宅','件', '団', '向', '老', '争', '任', '汚', '困', '条', 
 '判','風', '役', '労', '努', '均', '究', '投', '技', '身', '求','出', '妻', '命', '招', '官', '府', '治', '宗', '材', '存','表', '果', '受', '念', '非', '泊', '応', 
 '取', '具', '性','価', '泣', '並', '述', '保', '面', '示', '苦', '飛', '省','直', '祝', '逆', '師', '染', '研', '政', '葉', '珍', '郊','約', '相', '急', '信', '狭', 
 '疲', '達', '断', '将', '負','械', '容', '専', '挙', '値', '殺', '婚', '般', ' 差', '候','能', '座', '格', '残', '消', '案', '連', '個', '梁', '眠','軽', '済', '健', 
 '康', '異', '陸', '郵', '源', '探', '設','移', '球', '覚', '側', '術', '接', '略', '渡', '境', '責','機', '商', '深', '窓', '産', '率', '許', '情', '細', '痛','奥', 
 '満', '登', '絶', '植', '加', '進', '著', '貿', '等','然', '湖', '減', '並', '勤', '過', '喫', '結', '蓮', '落','備', '絡', '営', '期', '報', '悲', '製', '喜', '暖', 
 '想','試', '愛', '器', '戰', '禁', '笔', '煙', '準', '解', '資','際', '違', '織', '察', '緑', '算', '疑', '種', '博', '増','雑', '誌', '弱', '難', '環', '識', '観', 
 '態', '談', '線','警', '競', '職', '論', '類', '輸', '課', '億', '横', '権'
 ]


SL_kanji = ['—', '人', '二', '七', '八', '九', '十', '入', '山', '二','才', '川', '口', '土', '子', '女', '千', '万', '上', '下','大', '小', '日', '月', '木',
 '火', '水', '五', '六', '円','中', '手', '分', '文', '少', '午', '今', '友', 
 '父', '公','犬', '元', '天', '田', '広', '生', '立', '四', '本', '半','目', '石', '古', '母', '兄', '出', '右', '左', '北', '外','市', '白', '冬', '正', '号', '先', 
 '同', '州', '回', '全','次', '百', '年', '休', '好', '耳', '肉', '字', '安', '多','行', '毎', '会', '気', '有', '名', '早', '西', '地', '市','私', '図', '何', '男',
 '足', '花', '売', '近', '社', '來','見', '作', '言', '弟', '走', '住', '町', '村', '赤', '金','始', '例', '空', '泳', '知', '明', '学', '林', '雨', '物','長', '夜', 
 '英', '店', '国', '青', '姉', '妹', '歩', '東','所', '京', '茶', '美', '乗', '食', '昼', '前', '後', '海','室', '南', '思', '春', '秋', '点', '高', '島', '速','旅',
 '通', '帰', '書', '校', '時', '家', '勉', '夏', '魚', '都','終', '週', '静','閉', '強', '滞', '森', '暑', '寒', '番','病', '場', '間', '短', '飲', '買', '朝', '晚', 
 '飯', '開','道', '晴', '新', '鉄', '園', '数', '続', '暗', '話', '電','遠','楽', '聞', '様', '読', '語', '駅', '曜', '親', '薬','夕', '方', '切', '止', '内', '着', 
 '欠', '予', '心', '比','王', '反', '化', '世', '太', '引', '主', '力','必', '写','民', '台', '区', '平', '失', '牛', '以', '史', '去', '他','仕', '由','用', '法', 
 '式', '米', '危', '未', '昔', '忙','色', '当', 'ム', '寺', '蜜', '伝', '因', '成', '代', '両','死', '再', '在', '交', '自', '体', '位', '低', '助', '変','初', '君', 
 '完', '利', '返', '冷', '良', '決', '局', '忘','考', '対', '徒', '別', '門', '度', '各', '実', '医', '卒','的', '季', '彼', '若', '育', '使', '定','和', '事', '組',
 '者', '注', '服', '単', '発', '界', '待', '秒', '神', '昨','参','計', '客', '室', '持', '降', '県', '科', '映', '画','音', '送', '席', '洋', '活', '洗', '要', '品', 
 '便', '段','留', '展', '係', '重', '院', '庭', '配', '倍', '味', '酒','部', '料', '起', '借', '記', '員', '真', '紙', '蜜', '原','流', '動', '教', '転', '現', '族', 
 '第', '祭', '険', '習','問', '宿', '理', '遊', '悪', '特','遅', '経', '歌', '僕','絵', '給', '答', '貸', '温', '階', '勝', 'ハ', '最', '集','験', '慟', '授', '寝', 
 '費', '節', '漢', '業', '希', '意','感', '練', '橋', '歴', '説', '関', '望', '適', '銀', '館','調', '質', '題', '熱', '選', '顔', '願', '賛', '頭', '簡','々', '工', 
 '功', '夫', '不', '払', '礼', '可', '庁', '宅','件', '団', '向', '老', '争', '任', '汚', '困', '条', '判','風', '役', '労', '努', '均', '究', '投', '技', '身', '求',
 '出', '妻', '命', '招', '官', '府', '治','宗', '材', '存','表', '果', '受', '念', '非', '泊', '応', '取', '具', '性','価','泣', '並', '述', '保', '面', '示', '苦', 
 '飛', '省','直', '祝', '逆', '師',  '和', '事', '組','者', '注', '服', '単', '発', '界', '待', '秒', '神', '昨','参', '計', '客', '室', '持', '降', '県', '科', '映', 
 '画','音', '送', '席', '洋', '活', '洗', '要', '品', '便', '段','留', '展', '係', '重', '院', '庭', '配', '倍', '味', '酒','部', '料', '起', '借', '記', '員', '真', 
 '紙', '蜜', '原','流', '動', '教', '転', '現', '族', '第', '祭', '険', '習','問', '宿', '理', '遊', '悪', '特', '遅', '経', '歌', '僕','絵', '給', '答', '貸', '温', 
 '階', '勝', 'ハ', '最', '集','験', '慟', '授', '寝', '費', '節', '漢', '業', '希', '意','感', '練', '橋', '歴', '説', '関', '望', '適', '銀', '館','調', '質', '題', 
 '熱', '選', '顔', '願', '賛', '頭', '簡']
HL_Full = ['—', '人', '二', '七', '八', '九', '十', '入', '山', '二','才', '川', '口', '土', '子', '女', '千', '万', '上', '下','大', '小', '日', '月', '木',
 '火', '水', '五', '六', '円','中', '手', '分', '文', '少', '午', '今', '友', 
 '父', '公','犬', '元', '天', '田', '広', '生', '立', '四', '本', '半','目', '石', '古', '母', '兄', '出', '右', '左', '北', '外','市', '白', '冬', '正', '号', '先', 
 '同', '州', '回', '全','次', '百', '年', '休', '好', '耳', '肉', '字', '安', '多','行', '毎', '会', '気', '有', '名', '早', '西', '地', '市','私', '図', '何', '男',
 '足', '花', '売', '近', '社', '來','見', '作', '言', '弟', '走', '住', '町', '村', '赤', '金','始', '例', '空', '泳', '知', '明', '学', '林', '雨', '物','長', '夜', 
 '英', '店', '国', '青', '姉', '妹', '歩', '東','所', '京', '茶', '美', '乗', '食', '昼', '前', '後', '海','室', '南', '思', '春', '秋', '点', '高', '島', '速','旅',
 '通', '帰', '書', '校', '時', '家', '勉', '夏', '魚', '都','終', '週', '静','閉', '強', '滞', '森', '暑', '寒', '番','病', '場', '間', '短', '飲', '買', '朝', '晚', 
 '飯', '開','道', '晴', '新', '鉄', '園', '数', '続', '暗', '話', '電','遠','楽', '聞', '様', '読', '語', '駅', '曜', '親', '薬','夕', '方', '切', '止', '内', '着', 
 '欠', '予', '心', '比','王', '反', '化', '世', '太', '引', '主', '力','必', '写','民', '台', '区', '平', '失', '牛', '以', '史', '去', '他','仕', '由','用', '法', 
 '式', '米', '危', '未', '昔', '忙','色', '当', 'ム', '寺', '蜜', '伝', '因', '成', '代', '両','死', '再', '在', '交', '自', '体', '位', '低', '助', '変','初', '君', 
 '完', '利', '返', '冷', '良', '決', '局', '忘','考', '対', '徒', '別', '門', '度', '各', '実', '医', '卒','的', '季', '彼', '若', '育', '使', '定','和', '事', '組',
 '者', '注', '服', '単', '発', '界', '待', '秒', '神', '昨','参','計', '客', '室', '持', '降', '県', '科', '映', '画','音', '送', '席', '洋', '活', '洗', '要', '品', 
 '便', '段','留', '展', '係', '重', '院', '庭', '配', '倍', '味', '酒','部', '料', '起', '借', '記', '員', '真', '紙', '蜜', '原','流', '動', '教', '転', '現', '族', 
 '第', '祭', '険', '習','問', '宿', '理', '遊', '悪', '特','遅', '経', '歌', '僕','絵', '給', '答', '貸', '温', '階', '勝', 'ハ', '最', '集','験', '慟', '授', '寝', 
 '費', '節', '漢', '業', '希', '意','感', '練', '橋', '歴', '説', '関', '望', '適', '銀', '館','調', '質', '題', '熱', '選', '顔', '願', '賛', '頭', '簡','々', '工', 
 '功', '夫', '不', '払', '礼', '可', '庁', '宅','件', '団', '向', '老', '争', '任', '汚', '困', '条', '判','風', '役', '労', '努', '均', '究', '投', '技', '身', '求',
 '出', '妻', '命', '招', '官', '府', '治','宗', '材', '存','表', '果', '受', '念', '非', '泊', '応', '取', '具', '性','価','泣', '並', '述', '保', '面', '示', '苦', 
 '飛', '省','直', '祝', '逆', '師',  '和', '事', '組','者', '注', '服', '単', '発', '界', '待', '秒', '神', '昨','参', '計', '客', '室', '持', '降', '県', '科', '映', 
 '画','音', '送', '席', '洋', '活', '洗', '要', '品', '便', '段','留', '展', '係', '重', '院', '庭', '配', '倍', '味', '酒','部', '料', '起', '借', '記', '員', '真', 
 '紙', '蜜', '原','流', '動', '教', '転', '現', '族', '第', '祭', '険', '習','問', '宿', '理', '遊', '悪', '特', '遅', '経', '歌', '僕','絵', '給', '答', '貸', '温', 
 '階', '勝', 'ハ', '最', '集','験', '慟', '授', '寝', '費', '節', '漢', '業', '希', '意','感', '練', '橋', '歴', '説', '関', '望', '適', '銀', '館','調', '質', '題', 
 '熱', '選', '顔', '願', '賛', '頭', '簡','々', '工', '功', '夫', '不', '払', '礼', '可', '庁', '宅','件', '団', '向', '老', '争', '任', '汚', '困', '条', 
 '判','風', '役', '労', '努', '均', '究', '投', '技', '身', '求','出', '妻', '命', '招', '官', '府', '治', '宗', '材', '存','表', '果', '受', '念', '非', '泊', '応', 
 '取', '具', '性','価', '泣', '並', '述', '保', '面', '示', '苦', '飛', '省','直', '祝', '逆', '師', '染', '研', '政', '葉', '珍', '郊','約', '相', '急', '信', '狭', 
 '疲', '達', '断', '将', '負','械', '容', '専', '挙', '値', '殺', '婚', '般', ' 差', '候','能', '座', '格', '残', '消', '案', '連', '個', '梁', '眠','軽', '済', '健', 
 '康', '異', '陸', '郵', '源', '探', '設','移', '球', '覚', '側', '術', '接', '略', '渡', '境', '責','機', '商', '深', '窓', '産', '率', '許', '情', '細', '痛','奥', 
 '満', '登', '絶', '植', '加', '進', '著', '貿', '等','然', '湖', '減', '並', '勤', '過', '喫', '結', '蓮', '落','備', '絡', '営', '期', '報', '悲', '製', '喜', '暖', 
 '想','試', '愛', '器', '戰', '禁', '笔', '煙', '準', '解', '資','際', '違', '織', '察', '緑', '算', '疑', '種', '博', '増','雑', '誌', '弱', '難', '環', '識', '観', 
 '態', '談', '線','警', '競', '職', '論', '類', '輸', '課', '億', '横', '権'
 ]
HL_extra_kanji = ['々', '工', '功', '夫', '不', '払', '礼', '可', '庁', '宅','件', '団', '向', '老', '争', '任', '汚', '困', '条', 
 '判','風', '役', '労', '努', '均', '究', '投', '技', '身', '求','出', '妻', '命', '招', '官', '府', '治', '宗', '材', '存','表', '果', '受', '念', '非', '泊', '応', 
 '取', '具', '性','価', '泣', '並', '述', '保', '面', '示', '苦', '飛', '省','直', '祝', '逆', '師', '染', '研', '政', '葉', '珍', '郊','約', '相', '急', '信', '狭', 
 '疲', '達', '断', '将', '負','械', '容', '専', '挙', '値', '殺', '婚', '般', ' 差', '候','能', '座', '格', '残', '消', '案', '連', '個', '梁', '眠','軽', '済', '健', 
 '康', '異', '陸', '郵', '源', '探', '設','移', '球', '覚', '側', '術', '接', '略', '渡', '境', '責','機', '商', '深', '窓', '産', '率', '許', '情', '細', '痛','奥', 
 '満', '登', '絶', '植', '加', '進', '著', '貿', '等','然', '湖', '減', '並', '勤', '過', '喫', '結', '蓮', '落','備', '絡', '営', '期', '報', '悲', '製', '喜', '暖', 
 '想','試', '愛', '器', '戰', '禁', '笔', '煙', '準', '解', '資','際', '違', '織', '察', '緑', '算', '疑', '種', '博', '増','雑', '誌', '弱', '難', '環', '識', '観', 
 '態', '談', '線','警', '競', '職', '論', '類', '輸', '課', '億', '横', '権'
]

json_dict = {
    "SL Kanji":SL_kanji,
    "HL Kanji":HL_Full,
    "HL extra kanji": HL_extra_kanji
}

with open("ib kanji.json", "wb")as f:
    f.write(json.dumps(json_dict, ensure_ascii=False, indent=4).encode("utf-8"))