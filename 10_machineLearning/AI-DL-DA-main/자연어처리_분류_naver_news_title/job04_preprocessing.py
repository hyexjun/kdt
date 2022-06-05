import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle
from konlpy.tag import Okt


pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('./crawling_data/naver_news_220330.csv')  #아까 컨캣한 결과물을 df에 담는다.
# print(df.head())
# print(df.category.value_counts())
df.info()

X= df.title
Y= df.category

encoder = LabelEncoder()   #라벨 인코더 객체를 만들어서
labeled_Y= encoder.fit_transform(Y)   # 인코더 객체가 Y(카테고리)를 가지고 라벨인코딩을 한 객체가 labeled_Y. Y 결과값이 인코딩이 됐지.
# print(encoder.classes_)
# print(labeled_Y[:5])
# with open('./output/encoder.pickle', 'wb') as f:        
#     pickle.dump(encoder, f)

#encoder객체에는 지금 정치는 1, 사회는 2 이런식으로 라벨링에 대한 정보가 들어갔고
#labeled_Y는 그래서 결과인 Y를 1,1,1,3,2,2,5, 이런식으로 전환한 게 들어간 거지
# 그래서 encoder 객체를 저장하는 거임 나중에 쓰려고.



onehot_Y = to_categorical(labeled_Y)  # Y 라벨링한 거를  onehot인코더로 카테고리 분류함.
# print(onehot_Y)

okt = Okt()
# x = []
for i in range(len(X)):        #X의 길이  = title의 개수만큼
   X[i] = okt.morphs(X[i], stem=True)   #각각의 title을 형태소분리함.

stopwords= pd.read_csv('./crawling_data/stopwords.csv', index_col=0)



for j in range(len(X)):   # X[j]는 각각의 타이틀
   words =[]
   for i in range(len(X[j])):
      if len(X[j][i]) > 1:  #두글자부터만 보겠다.   X[j]의 i번째는, 각각의 타이틀에서 각각의 토큰을 의미함.
         if X[j][i] not in list(stopwords['stopword']):  #그중에서도 불용어에 포함 안 되는 애들만
            words.append(X[j][i])   # 그렇게 찾은거를 words리스트에 넣음 (분석에 사용할 것들.)
   X[j] = ' '.join(words)   #그리고 다시 X[j]를 그렇게 사용할 단어로만 찾은 것으로 교체함.
print(X[1])




token = Tokenizer()
token.fit_on_texts(X)   # 이 X안에 있는 모든 토큰화된 단어를 찾아서 라벨링을 해줌. 그래서 X의 다른 row의 같은 단어는 같은 라벨링임. 딕셔너리로 하고.
  
  #fit_on_texts를 했으니까 token객체에 X의 변환된 정보 딕셔너리가 들어가 있음. 이 token을 저장함. 이 token에 지금 X에 들어간 모든 단어 라벨링 한 정보가 들어가 있다!
  
  #tokened_X는 아직 저장안해. 전처리 해줘야함. 길이도 맞춰야하고 트레이닝 셋 테스트셋 나누기도 해야하고.

tokened_X = token.texts_to_sequences(X)   #리스트로 들어감.
print(tokened_X[1])

with open('./output/news_token.pickle', 'wb') as f:
   pickle.dump(token, f)   #피클로 토큰 저장해놓자 .. 근데 왜 token만 저장 ? tokened_X가 아니고?

wordsize = len(token.word_index) + 1   #토큰해놓은 건 인덱스는 0없고 1부터인데, 우리가 0을 쓸 거라서 (?) +1을 함. 문장 자리수 맞추려고 앞에 0 채우는 거임.

print('wordsize', wordsize)
# print(token.word_index)

max = 0
for i in range(len(tokened_X)):  #tokened_X  (토큰화된 X)의 길이들 하나씩 확인해서
   if max < len(tokened_X[i]):
      max = len(tokened_X[i])
print(max)  #최대 길이 찾음.


X_pad = pad_sequences(tokened_X, max)  #각 tokened_X를 맥스값 맞춰서 패드 넣어준게 X_pad다.
print(X_pad[:5])

X_train, X_test, Y_train, Y_test = train_test_split(         #패드 넣어준 X_pad가 입력값이고  원핫으로 인코딩한 onehot_Y가 정답값
   X_pad, onehot_Y, test_size = 0.1)

print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

xy= X_train, X_test, Y_train, Y_test
np.save('./crawling_data/news_data_max_{}_wordsize_{}'.format(max,wordsize), xy)   #데이터셋 나눈 거 저장해놓는다.


