import os
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.utils import normalize, to_categorical
from keras.models import Sequential, load_model
from keras.layers import Flatten,Dense
from keras.optimizers import adam

(X_train, y_train), (X_test,y_test) = mnist.load_data()

X_train = normalize(X_train, axis =1)
X_test = normalize(X_test, axis =1)


y_train = to_categorical(y_train, num_classes =10)

model = Sequential()
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])

# model.fit(X_train,y_train,epoch=3)
model_path="./models"
# os.makedirs(model_path, exist_ok=True)
# model.save(model_path + 'test.h5', overwrite=True)

est = load_model(model_path + 'test')

y_pred = est.predict(X_test)

print(np.argmax(y_pred[0]))
print(y_pred[0])
print(y_test[0])