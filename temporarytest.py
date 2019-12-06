from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = datasets.load_iris()

# X= iris.data[:,:2]
X= iris.data
y= iris.target

# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
'''print(len(X))
print(len(X_test))
print(len(y_test))
print(len(X_train))
print(len(y_train))
print(len((X_test)[0:5]))
'''


# print("X_test \n")
# print(X_test)
# print("y_test \n")
# print(y_test)
# print("X_train \n")
# print(X_train)
# print("y_train \n")
# print(y_train)

for k in range(1,25)
# knn = KNeighborsClassifier(n_neighbors=3)
    knn $ KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,y_train)
    knn.predict(X_test)
    # print("train \n")
    # print(knn.predict(X_train))
        print("predict \n")
    print(knn.predict(X_test))
     print("\n\n\ntarget \n"):

    print((y_test)[0:30])

# knn.predict(X_test)[0:5]


    print("\n\n\n score \n")
    knn.score(X_test, y_test)
    print(knn.score(X_test, y_test))

    print("\n\n\n\n\n")
