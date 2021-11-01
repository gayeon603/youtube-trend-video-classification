"""워드클라우드"""

import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

data = pd.read_csv("/content/results.csv")

title = data[data['trend'] == 1]

title = title['title']

title_list = np.array(title.to_list())

string = ""
for i, st in enumerate(title_list):
  string += st+' '

stopwords = set(STOPWORDS) 
stopwords.add('feat') 
stopwords.add('ft')
stopwords.add('EP')
stopwords.add('VS')
stopwords.add('있는')
stopwords.add('하는')
stopwords.add('없는')
stopwords.add('1부')
stopwords.add('nan')
stopwords.add('ver')
stopwords.add('2탄')
stopwords.add('ㅋㅋㅋㅋㅋ')

wordcloud = WordCloud(font_path='/content/BMHANNAPro.ttf',stopwords=stopwords,background_color='white', colormap = "Accent_r", width=1500, height=1000).generate(string)

plt.figure(figsize=(100,100))
plt.imshow(wordcloud)
