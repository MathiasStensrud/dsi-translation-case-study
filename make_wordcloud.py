# https://www.geeksforgeeks.org/generating-word-cloud-python/
# pip install matplotlib
# pip install pandas
# pip install wordcloud
# Python program to generate WordCloud

# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reads 'Youtube04-Eminem.csv' file
# df = np.loadtxt(r'nob.txt')
colnames=['English', 'French']
# df = pd.read_csv(r'nob.txt', encoding ="latin-1", delimiter='\t', header=None, names=colnames)
df = pd.read_csv(r'fra.txt', delimiter='\t', header=None, names=colnames)
colnames_FR = ['word']
# df = df.loc[:100]
df_FR_stop = pd.read_csv(r'french_stop.txt', header=None, names=colnames_FR)

FR_stop_series = pd.Series(df_FR_stop.loc[:, 'word'])
stopwords_FR = set(FR_stop_series)

# # df = df.iloc[:50000]
# df_motive = df[['motive']]
# df_motive.dropna(inplace = True)

comment_words = ' '
# stopwords = set(STOPWORDS)
stopwords = stopwords_FR
# iterate through the csv file
for val in df.French:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    for words in tokens:
        comment_words = comment_words + words + ' '


wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
# plt.savefig('Eng_wordcloud')
# plt.savefig('FR_wordcloud')
