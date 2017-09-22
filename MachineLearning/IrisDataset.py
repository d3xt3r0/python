from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()
#print iris.feature_names
#print iris.target_names
#print iris.data[0]
#print iris.target[49]
test_idx = [0,50,100]

train_label = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

test_data = iris.data[test_idx]
test_label = iris.target[test_idx]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_label)

print test_label
print test_data
print clf.predict(test_data) 