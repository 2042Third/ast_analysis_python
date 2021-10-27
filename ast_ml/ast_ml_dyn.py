{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a39780d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.metrics import precision_score\n",
    "from sklearn.multioutput import MultiOutputClassifier\n",
    "# example of making a single class prediction\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.neural_network import MLPClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "618e471e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#ast data\n",
    "ad = pd.read_csv('new.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "962a5699",
   "metadata": {},
   "source": [
    "## Functional and Dynamic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8ab09bee",
   "metadata": {},
   "outputs": [],
   "source": [
    "trainxor = ad[['Dyn', \"Func\"]]\n",
    "trainyor = ad[['Relatedness']]\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    trainxor, trainyor, test_size=0.1, random_state=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4d6e17b2",
   "metadata": {},
   "source": [
    "### Bayesian"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a19de907",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.65181384 0.65168534 0.6553915  0.65936667 0.6712922  0.68321772\n",
      " 0.69116807]\n"
     ]
    }
   ],
   "source": [
    "from sklearn import linear_model\n",
    "\n",
    "reg = linear_model.BayesianRidge()\n",
    "dn, fc = 0, 3\n",
    "model = reg.fit(X_train, y_train.values.ravel())\n",
    "xnew = [[0,1],[1,0],[0,10],[0,20],[0,50],[0,80],[0,100]]\n",
    "y_pred = model.predict(xnew)\n",
    "print(y_pred)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f3a6707",
   "metadata": {},
   "source": [
    "### Gaussian "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "54cb69a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.67      0.99      0.80       978\n",
      "           1       1.00      0.76      0.86      1980\n",
      "\n",
      "    accuracy                           0.83      2958\n",
      "   macro avg       0.83      0.87      0.83      2958\n",
      "weighted avg       0.89      0.83      0.84      2958\n",
      "\n",
      "[[ 971    7]\n",
      " [ 482 1498]]\n",
      "Precision score: 0.9953488372093023\n",
      "X=[0, 1], Predicted=[1.0, 0.0]\n",
      "X=[1, 0], Predicted=[0.0, 1.0]\n",
      "X=[0, 10], Predicted=[1.0, 0.0]\n",
      "X=[0, 20], Predicted=[1.0, 0.0]\n",
      "X=[0, 50], Predicted=[1.0, 0.0]\n",
      "X=[0, 80], Predicted=[1.0, 0.0]\n",
      "X=[0, 100], Predicted=[0.0, 1.0]\n"
     ]
    }
   ],
   "source": [
    "gnb = GaussianNB()\n",
    "dn, fc = 0, 3\n",
    "model = gnb.fit(X_train, y_train.values.ravel())\n",
    "y_pred = model.predict(X_test)\n",
    "print(classification_report(y_test,y_pred))\n",
    "print(confusion_matrix(y_test, y_pred))\n",
    "print(\"Precision score: {}\".format(precision_score(y_test,y_pred)))\n",
    "xnew = [[0,1],[1,0],[0,10],[0,20],[0,50],[0,80],[0,100]]\n",
    "xprobs = model.predict_proba(X_test)\n",
    "for i in range(len(xnew)):\n",
    "\tprint(\"X=%s, Predicted=%s\" % (xnew[i], [round(xprobs[i][0],3),round(xprobs[i][1],3)]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7421decb",
   "metadata": {},
   "source": [
    "### Logistic Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "aee6389e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.68      0.98      0.80       978\n",
      "           1       0.99      0.77      0.86      1980\n",
      "\n",
      "    accuracy                           0.84      2958\n",
      "   macro avg       0.83      0.87      0.83      2958\n",
      "weighted avg       0.88      0.84      0.84      2958\n",
      "\n",
      "[[ 958   20]\n",
      " [ 457 1523]]\n",
      "Precision score: 0.9870382372002592\n",
      "X=[0, 1], Predicted=[0.648, 0.352]\n",
      "X=[1, 0], Predicted=[0.0, 1.0]\n",
      "X=[0, 10], Predicted=[0.706, 0.294]\n",
      "X=[0, 20], Predicted=[0.692, 0.308]\n",
      "X=[0, 50], Predicted=[0.702, 0.298]\n",
      "X=[0, 80], Predicted=[0.711, 0.289]\n",
      "X=[0, 100], Predicted=[0.0, 1.0]\n"
     ]
    }
   ],
   "source": [
    "logreg = LogisticRegression()\n",
    "dn, fc = 0, 3\n",
    "model = logreg.fit(X_train, y_train.values.ravel())\n",
    "y_pred = model.predict(X_test)\n",
    "print(classification_report(y_test,y_pred))\n",
    "print(confusion_matrix(y_test, y_pred))\n",
    "print(\"Precision score: {}\".format(precision_score(y_test,y_pred)))\n",
    "xnew = [[0,1],[1,0],[0,10],[0,20],[0,50],[0,80],[0,100]]\n",
    "xprobs = model.predict_proba(X_test)\n",
    "for i in range(len(xnew)):\n",
    "\tprint(\"X=%s, Predicted=%s\" % (xnew[i], [round(xprobs[i][0],3),round(xprobs[i][1],3)]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "103d9686",
   "metadata": {},
   "source": [
    "### Neural Network"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3e740052",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.71      0.85      0.77       978\n",
      "           1       0.92      0.83      0.87      1980\n",
      "\n",
      "    accuracy                           0.84      2958\n",
      "   macro avg       0.81      0.84      0.82      2958\n",
      "weighted avg       0.85      0.84      0.84      2958\n",
      "\n",
      "[[ 836  142]\n",
      " [ 344 1636]]\n",
      "Precision score: 0.9201349831271091\n",
      "X=[0, 1], Predicted=[0.493, 0.507]\n",
      "X=[1, 0], Predicted=[0.0, 1.0]\n",
      "X=[0, 10], Predicted=[0.724, 0.276]\n",
      "X=[0, 20], Predicted=[0.615, 0.385]\n",
      "X=[0, 50], Predicted=[0.69, 0.31]\n",
      "X=[0, 80], Predicted=[0.755, 0.245]\n",
      "X=[0, 100], Predicted=[0.0, 1.0]\n"
     ]
    }
   ],
   "source": [
    "mlpc=MLPClassifier(hidden_layer_sizes=(11,11,11),max_iter=500)\n",
    "model = mlpc.fit(X_train, y_train.values.ravel())\n",
    "y_pred = model.predict(X_test)\n",
    "print(classification_report(y_test,y_pred))\n",
    "print(confusion_matrix(y_test, y_pred))\n",
    "print(\"Precision score: {}\".format(precision_score(y_test,y_pred)))\n",
    "xnew = [[0,1],[1,0],[0,10],[0,20],[0,50],[0,80],[0,100]]\n",
    "xprobs = model.predict_proba(X_test)\n",
    "for i in range(len(xnew)):\n",
    "\tprint(\"X=%s, Predicted=%s\" % (xnew[i], [round(xprobs[i][0],3),round(xprobs[i][1],3)]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "875e4d81",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80cc15c4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
