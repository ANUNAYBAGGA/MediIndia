from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
def randomforest(L):
    dataset_train = pd.read_csv('Training.csv')
    dataset_test = pd.read_csv('Testing.csv')

    x_train = dataset_train.iloc[:,0:132]
    y_train = dataset_train.iloc[:,132]
    print(L)
    x_test = dataset_test.iloc[:,0:132]
    y_test = dataset_test.iloc[:,132]

    clf = RandomForestClassifier(n_jobs = 2 , random_state = 0)
    clf.fit(x_train,y_train)
    df = pd.DataFrame({'':L})
    df = df.transpose()
    print(df)

    y = clf.predict(df)
    print(y)
    #print(y_test)
    #print("Accuracy - " , accuracy_score(y_test,y))
    return y
