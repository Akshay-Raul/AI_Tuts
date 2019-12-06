
import numpy as np
import matplotlib.pyplot as plt


from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.tree.export import export_text
###########

from sklearn.model_selection import train_test_split
from sklearn import metrics 

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
# Parameters
n_classes = 3
plot_colors = "ryb"
plot_step = 0.02

# Load data
iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test, y_train,y_test = train_test_split(X,y, test_size=0.2)


clf = DecisionTreeClassifier(criterion="entropy")
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print(metrics.confusion_matrix(y_test,y_pred))

print("Single Tree Accuracy" + str(metrics.accuracy_score(y_test,y_pred)))

'''
clf = RandomForestClassifier(n_estimators=50,criterion="entropy",max_depth=3)
clf.fit(X_train,y_train)


values=[]


for est in clf.estimators_:
	print(export_text(est,iris.feature_names))
	y_pred = est.predict(X_test)
	acc_score = metrics.accuracy_score(y_test,y_pred)
	values.append(acc_score)
	print(acc_score)
	print(metrics.confusion_matrix(y_test,y_pred))
'''

# y_pred = clf.predict(X_test)

# print("Mean Forest Prediction Acc:" + str(np.mean(values)))
# print("Actual Forest Prediction Acc:" + str(metrics.accuracy_score(y_test,y_pred)))