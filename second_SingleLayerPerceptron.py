import os

from sklearn.linear_model import Perceptron
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from joblib import dump, load

iris = load_iris()

X = iris.data
y= iris.target

X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=0.2)
filename = './saved_model/two_file.sav'
model= Perceptron()

model.fit(X_train, y_train)
joblib.dump(model, filename)
# joblib.dump(X, 'reg_1.sav')
clf = joblib.load("./saved_model/two_file.sav")

# clf = MLPClassifier(activate='relu', solver='sgd', hidden_layer_sizes=(10,5))
# clf2 = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(10,5))

# clf= Perceptron()

# clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(accuracy_score(y_test,y_pred))
