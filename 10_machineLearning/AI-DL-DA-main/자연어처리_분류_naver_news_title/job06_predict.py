import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle
from tensorflow.keras.models import load_model
from konlpy.tag import Okt




pd.set_option('display.unicode.east_asian_width', True)   #텍스트 정렬 맞춤
df = pd.read_csv('./crawling_data/naver_headline_news220331.csv')  #헤드라인 불러옴
print(df.head()) 


X= df.title   #타이틀 입력값
Y= df.category   #카테고리는 정답값

# encoder = LabelEncoder()   이렇게 만들지말고 저장했던 거 불러와야지
with open('./output/encoder.pickle', 'rb') as f:
    encoder = pickle.load(f)

labeled_Y= encoder.transform(Y)   #헤드라인의 카테고리를 인코더로 라벨링함
'''fit_transform은 y를 주면 y의 유니크한 값을 찾음 그럼 카테고리 6개지?  근데 그거 정했잖아.
그거 정한 걸로 그대로 오늘꺼 써야하잖아. 이미 정해진 걸로 라벨링만 작업할거면 transform해야함.'''
'''#라벨을 주고 그 라벨이 뭐냐 물어볼때는 리버스트랜스폼'''

print(encoder.classes_)
print(labeled_Y[:5])





onehot_Y = to_categorical(labeled_Y)  #라벨링한걸 다시 원핫인코더로
# print(onehot_Y)

okt = Okt()
# x = []
for i in range(len(X)):
   X[i] = okt.morphs(X[i], stem=True)   #각 타이틀 (row)를 형태소분리

stopwords= pd.read_csv('./crawling_data/stopwords.csv', index_col=0)

for j in range(len(X)):
   words =[]
   for i in range(len(X[j])):
      if len(X[j][i]) > 1:  #두글자부터만 보겠다
         if X[j][i] not in list(stopwords['stopword']):  #그중에서도 불용어에 포함 안 되는 애들만
            words.append(X[j][i])
   X[j] = ' '.join(words)  # 형태소 분리한 것중에서도 불용어 뺀 것으로 정리
print(X[1])



# 학습 안 한 단어가 오면 0이 옴.

with open('./output/news_token.pickle', 'rb') as f:
    token = pickle.load(f)   # 토큰 저장해놨던 거 불러와
tokened_X = token.texts_to_sequences(X)   #타이틀을 저장한 토큰으로 토크나이징 함

for i in range(len(tokened_X)):   # row의 개수
    
    if len(tokened_X[i]) > 29: #맥스값        #각 row의 토큰의 길이가 29보다 크면 - 즉 오늘 헤드라인 확인하려는 건데, 그 헤드라인이 29보다 크면
        tokened_X[i] = tokened_X[i][:29]         #앞부분을 버려
        
        
X_pad = pad_sequences(tokened_X, 29)   # 맥스값 맞춰서 패딩 넣어주고

label = encoder.classes_  #위에서 인코더 불러왔었지. 거기에 저장된 클래스 정보 (카테고리 정보) 가져옴.

model = load_model('./output/news_category_classification_model_0.798705518245697.h5')   #만들었던 모델 불러온다
preds = model.predict(X_pad)  # 그 모델로 패딩넣은 X값 넣어서 예측해보자
predicts =[]
for pred in preds:
    predicts.append(label[np.argmax(pred)])   #X값 넣어서 예측한 것 중 가장 확률 높은 거를 label 클래스로 전환해서 predicts에 넣는다.

df['predict'] = predicts   #predict컬럼 만들어서 predicts 값 넣는다
df['OX'] = 0   #OX컬럼도 만든다 일단 0으로 초기화해놓고

for i in range(len(df)):
    if df.loc[i, 'category'] == df.loc[i, 'predict']:   #카테고리랑 예측한 게 맞으면 O, 아니면 X 넣어라
        df.loc[i,'OX'] = 'O'
    else:
        df.loc[i,'OX'] = 'X'
print(df['OX'].value_counts()/len(df))

for i in range(len(df)):
    if df['category'][i] != df['predict'][i]:
        print(df.iloc[i])









