import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

df = pd.read_csv('breast-cancer-wisconsin.data', delimiter=',', header=None)
df = df.replace('?', np.nan)
df = df.dropna()
df = df.drop(0, axis=1)

data = df.iloc[:, :-1]
kelas = df.iloc[:, -1]
print(data)
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
score = cross_val_score(knn, data, kelas, cv=10, scoring='accuracy')
print(score)