from PIL import Image
import glob
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('../models/cat_and_dog_binary_classification0.7972000241279602.h5')
model.summary()
img_dir = '../datasets/train/'
image_w = 64
image_h = 64
categories = ['cat', 'dog']

dog_files = glob.glob(img_dir + 'dog*')
dog_sample = np.random.randint((len(dog_files)))
dog_sample_path = dog_files[dog_sample]

print(dog_sample_path)

try:
    img = Image.open(dog_sample_path)
    img.show()
    img = img.convert('RGB')
    img = img.resize((image_w, image_h))
    data = np.asarray(img) # type을 바꿔준다, array -> 새로 만든다
    data = data / 255
    dog_data = data.reshape(1, 64, 64, 3)
except:
    print('error')
print(categories[int(model.predict(dog_data).round()[0][0])])