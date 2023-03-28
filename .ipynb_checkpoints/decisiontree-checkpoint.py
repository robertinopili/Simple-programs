from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree

data = load_iris()
X, y = data.data, data.target
clf = DecisionTreeClassifier()
clf.fit(X, y)

fig = plt.figure(figsize=(50, 30))
_ = tree.plot_tree(clf, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.show()