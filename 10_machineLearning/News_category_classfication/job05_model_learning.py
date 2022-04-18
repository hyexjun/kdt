import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

X_train, X_test, Y_train, Y_text = np.load('./crawling_data/news_data_max_29_wordsize_12740.npy', allow_pickle=True)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_text.shape)

model = Sequential()
model.add(Embedding(12740, 300, input_length=29))  # 12740차원을..다룬다..
