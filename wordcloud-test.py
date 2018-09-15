import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#background_imag = plt.imread('51452-106.jpg')
f = open('大唐万户侯.txt','r',encoding = 'utf-8')
txt = f.read()
words = jieba.lcut(txt)
newtxt = ''.join(words)
wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\simkai.ttf').generate(newtxt)
wordcloud.to_file('词云效果图.png')
