from sklearn import tree

# Examples
# Weight Texture Label
# 150g   Bumpy   Orange
# 170g   Bumpy   Orange
# 140g   Smooth  Apple
# 130g   Smooth  Apple

# Training Data
# features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]  # Input to classifier
features = [[140, 1], [130, 1], [150, 0], [170, 0]]  # scikit-learn uses real-valued features
# labels = ["apple", "apple", "orange", "orange"]  # Desired output
labels = [0, 0, 1, 1]

# Train Classifer
clf = tree.DecisionTreeClassifier()  # Decision Tree classifier
clf = clf.fit(features, labels)  # Find patterns in data
x=input("Enter weight")
y=input("Enter 1 if smooth 0 if bumpy")
# Make Predictions
if clf.predict([x, y]):
	print "orange"
else:
	print "Apple"
# Output: 0-apple, 1-orange
# Correct output is: 1-orange
