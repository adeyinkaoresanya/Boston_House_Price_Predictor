from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import pickle


data = load_boston()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)
classifier = GradientBoostingRegressor()
classifier.fit(X_train, y_train)

with open("classifier.pkl", "wb") as f:
    pickle.dump(classifier, f)