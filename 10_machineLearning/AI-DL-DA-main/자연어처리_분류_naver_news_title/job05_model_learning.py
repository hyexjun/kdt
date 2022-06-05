import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

X_train, X_test, Y_train, Y_test =  np.load(
    './crawling_data/news_data_max_29_wordsize_12831.npy', allow_pickle=True
)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

model = Sequential()
model.add(Embedding(12831, 300, input_length= 29))  #embedding 레이어 : 처음 넣는 거는 총 단어의 개수. input_length에는 아까 max값. 29개 들어간다.
 # 트레이닝 단어는 12831. row값이 아님! 총 단어 개수임! 단어를 학습해야하니까.
 #임베딩 단어의 의미축 ???????????????????? 더 알아봐야할 듯.
# 13904 차원 너무 많으니까 그걸 300차원으로 줄이라고.
model.add(Conv1D(32, kernel_size=5, padding='same', activation='relu'))  #위치관계 파악해서 빠르게 본다.  앞뒤관계를 학습한다 ??????????????
model.add(MaxPooling1D(pool_size=1))
model.add(LSTM(128, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(6, activation='softmax'))  #다중분류기니까
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])  #분류니까 loss는 카테고리


fit_hist= model.fit(X_train, Y_train, batch_size=100, epochs=10,verbose=1, validation_data = (X_test, Y_test))
model.save('./output/news_category_classification_model_{}.h5'.format(fit_hist.history['val_accuracy'][-1]))
plt.plot(fit_hist.history['accuracy'][5:], label='accuracy')
plt.plot(fit_hist.history['val_accuracy'][5:], label='val_accuracy')
plt.legend()
plt.show()

#
# pred= model.predict(X_test)
# plt.plot(Y_test, label='actual')
# plt.plot(pred, label='predict')
# plt.show()