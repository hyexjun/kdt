import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

form_window = uic.loadUiType('./mainWidget.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.path = None
        self.setupUi(self)
        self.model = load_model('../models/cat_and_dog_binary_classification0.7972000241279602.h5')

        self.btn_select.clicked.connect(self.predict_image)

    def predict_image(self):
        self.path = QFileDialog.getOpenFileName(
            self,
            "Open file", 'C:\work\python\ML_exam\datasets',
            "Image Files(*.jpg);;All Files(*.*);;Text fil(*.txt)"
        )
        print(self.path)
        if self.path[0]:
            pixmap = QPixmap(self.path[0])
            self.lbl_image.setPixmap(pixmap)

            try:
                img = Image.open(self.path[0])
                img = img.convert('RGB')
                img = img.resize((64,64))
                data = np.asarray(img)
                data = data / 255
                data = data.reshape(1,64,64,3)
            except:
                  print('error')
            predict_value = self.model.predict(data)
            if predict_value > 0.5:
                self.lbl_predict.setText('이 이미지는 ' +
                   str((predict_value[0][0] * 100).round()) + '% 확률로 Dog입니다.')
            else:
                self.lbl_predict.setText('이 이미지는 ' +
                   str(((1 - predict_value[0][0]) * 100).round()) + '% 확률로 Cat입니다.')

app = QApplication(sys.argv)
mainWindow = Exam()
mainWindow.show()
sys.exit(app.exec_())