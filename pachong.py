import requests
from bs4 import BeautifulSoup
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence
import numpy as np


def spider(url, headers):
    with open('renming.txt', 'w', encoding='utf8') as fp:
        r = requests.get(url, headers=headers)
        r.encoding = 'gb2312'
        soup = BeautifulSoup(r.text, "html.parser")
        for news_list in soup.find_all(class_="list14"):
            content = news_list.text.strip()
            fp.write(content)
        fp.close()


def analyse():
    coco = open('renming.txt', encoding='utf-8').read()
    result = jieba.analyse.textrank(coco, topK=150, withWeight=True)
    alice_coloring = np.array(Image.open("./rmrb.jpeg"))
    keywords = dict()
    for i in result:
        keywords[i[0]] = i[1]
    print(keywords)
    wc = WordCloud(font_path='./fonts/simhei.ttf', background_color='White', max_words=150, mask=alice_coloring)
    wc.generate_from_frequencies(keywords)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    wc.to_file('rmrb.png')


if __name__ == "__main__":
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    url = 'http://www.people.com.cn/'
    spider(url, headers)
    analyse()

