import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.multioutput import MultiOutputClassifier

#ast data
ad = pd.read_csv('new.csv')

trainxor = ad[['Dec', "Func"]]
trainyor = ad[['Relatedness']]
# trainx = ad[['Dyn']]
# trainy = ad[[ "Func", 'DynFunc']]
count =0

X_train, X_test, y_train, y_test = train_test_split(
    trainxor, trainyor, test_size=0.1, random_state=0)


gnb = GaussianNB()
dn, fc = 0, 3
model = gnb.fit(X_train, y_train.values.ravel())
y_pred = model.predict(X_test)
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test, y_pred))
xnew = [[0, 0], [1, 0], [0, 1]]
ynew = model.predict_proba(xnew)
for i in range(len(xnew)):
	print("X=%s, Predicted=%s" % (xnew[i], ynew[i]))

while True:
  dn, fc = [int(x) for x in input("Next prediction\n").split(',')]
  y_pred = model.predict([[dn, fc]])
  print("Predict [%d, %d] %d" % (dn, fc, y_pred))
# print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
