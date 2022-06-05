import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # scikit-learn
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle
from konlpy.tag import Kkma, Okt
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('./crawling_data/naver_headline_news220331.csv')
print(df.head())

X = df.title
Y = df.category

with open('./output/encoder.pickle', 'rb') as f:
    encoder = pickle.load(f)
labeled_Y = encoder.transform(Y)
print(encoder.classes_)
print(labeled_Y[:5])

onehot_Y = to_categorical(labeled_Y)
print(onehot_Y)

okt = Okt()
for i in range(len(X)):
    X[i] = okt.morphs(X[i], stem=True)

stopwords = pd.read_csv('./crawling_data/stopwords.csv',
                        index_col=0)
for j in range(len(X)):
    words = []
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if X[j][i] not in list(stopwords['stopword']):
                words.append(X[j][i])
    X[j] = ' '.join(words)
print(X[1])

with open('./output/news_token.pickle', 'rb') as f:
    token = pickle.load(f)
tokened_X = token.texts_to_sequences(X)

for i in range(len(tokened_X)):
    if len(tokened_X[i]) > 29:
        tokened_X[i] = tokened_X[i][:29]
X_pad = pad_sequences(tokened_X, 29)
