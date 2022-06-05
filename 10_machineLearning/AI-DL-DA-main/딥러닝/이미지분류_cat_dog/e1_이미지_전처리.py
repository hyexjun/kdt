from PIL import Image
import glob
import numpy as np
from sklearn.model_selection import train_test_split

img_dir= '../datasets/train/'
categories = ['cat', 'dog']



image_w = 64
image_h =64

pixel = image_h * image_w * 3  #색 3개라서 3 곱함
X= []
Y= []
files = None

for idx, category in enumerate(categories):
    files = glob.glob(img_dir + category + '*')  #glob는 지정된 경로 안에 이 파일명 조건 만족하는 것들의 리스트를 받아온다.
    for i, f in enumerate(files):
        try:
            img = Image.open(f)   #파일 연다 (이미지객체)
            img = img.convert('RGB')   #rgb 비트맵 파일로 바꾼다
            img = img.resize((image_w, image_h))  #사이즈를 동일하게 맞춘다. 가로세로를 튜플로 받은 거임.
            data = np.asarray(img)  #넘파이의 array타입으로 바꾼다.
            X.append(data)  #데이터를 X리스트에 추가한다.
            Y.append(idx)
            if i % 300 ==0 :
                print(category, ':', f)   #걍 300번에 한번씩 진행사항 프린트 하게 한 거임.
        except:
            print(category, i, f)
X= np.array(X)
Y= np.array(Y)
print(X[0])
print(Y[:5])

X = X/ 255  #입력은 스케일링 하는 게 맞지. X의 값이 rgb값이 255까지라서.
# Y = Y/255  #근데 Y는 sigmoid니까 0아니면 1이잖아. 근데 이걸 255로 나누면 안 됐지. 이러면 다 결과가 0(혹은 0에 근접)이니까. 학습이 잘 안된다.
#라벨링이 잘못되면 학습이 안 된다 !

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size= 0.1
)

xy = (X_train, X_test, Y_train, Y_test)
np.save('../datasets/binary_image_data.npy', xy)