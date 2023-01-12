import pandas as pd
import jieba
from tqdm import tqdm
from wordcloud import WordCloud

data = pd.read_csv("clean.csv")
result = ''
text = data['comment'].astype(str)
for i in tqdm(text):
    wordlist = jieba.lcut_for_search(i)
    result+=(' '.join(wordlist))

# 设置停用词
stop_words = ['你', '我', '的', '了', '们', '就', '是', '和', '没有', '也', '在', '还', '不', '有', '好', '都', '没', '很', '，', '。', '！',
              '：', '？', '、', '.', '（',
              '）', '；','br','他','她','而','被','x20','x0A']
ciyun_words = ''

# 过滤后的词
for word in tqdm(result):
    if word not in stop_words:
        ciyun_words += word

wc = WordCloud(
    font_path='msyh.ttc',  # 中文
    background_color='white',  # 设置背景颜色为白色
    width=1000,
    height=700,
)
# 根据文本数据生成词云
wc.generate(ciyun_words)
# 保存词云文件
wc.to_file('img.jpg')
