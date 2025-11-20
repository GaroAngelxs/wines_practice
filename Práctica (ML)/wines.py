from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

wine = load_wine()
x, y = wine.data, wine.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Modelo 1: profundidad con limite (max_depth=2) ")
clf = DecisionTreeClassifier(max_depth=2, random_state=42)
clf.fit(x_train, y_train)

rules = export_text(clf, feature_names=list(wine.feature_names))
print(rules)

print("Precision en datos de prueba:", clf.score(x_test, y_test))
print("\nModelo 2: (No tiene limite) (max_depth=None)")
clf_no_limit = DecisionTreeClassifier(max_depth=None, random_state=42)
clf_no_limit.fit(x_train, y_train)

rules_no_limit = export_text(clf_no_limit, feature_names=list(wine.feature_names))
print(rules_no_limit)


print("Precisión en datos de prueba:", clf_no_limit.score(x_test, y_test))