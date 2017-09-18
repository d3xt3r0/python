__author__ = d3xt3r0

from sklearn import tree
from sklearn import neighbors,naive_bayes,svm


x = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,39],[171,75,42],[181,85,43]]
y = ['male','female','female','female','male','male','male','female','male','female','male']

#decition tree clasifier

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y);
predict = clf.predict([[190,70,43]])
print predict

#KNeighborsClassifier

clf1 = neighbors.KNeighborsClassifier()
clf1 = clf1.fit(x, y)
predict1 = clf1.predict([[190,70,43]])
print predict1

#GaussianNB

clf2 = naive_bayes.GaussianNB()
clf2 = clf2.fit(x, y)
predict2 = clf2.predict([[190,70,43]])
print predict2

#SVC

clf3 = svm.SVC()
clf3 = clf3.fit(x, y)
predict3 = clf3.predict([[190,70,43]])
print predict3