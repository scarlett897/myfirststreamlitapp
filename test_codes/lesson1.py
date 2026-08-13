
#activity 1
students=["Alice", "Bob", "Charlie", "David"]
scores=[85, 90, None, 70]
def avg_score(scores):
    numscores=[]
    for s in scores:
        if isinstance(s, (int, float)):
            numscores.append(s)
    avg1 = sum(numscores) / len(numscores)
    return avg1
avg=avg_score(scores)
for i in range(len(scores)):
    if scores[i] is None:
        scores[i] = round(avg, 2)

#activity 2
#program breaks because there is a string in a list of integers
scores=[85, 90, "N/A", 70]
numscores=[]
for i in range(len(scores)):
    if isinstance(scores[i], str):
        scores[i]=round(avg, 2)
print(scores)

#activity 3
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Bob', 'Charlie'],
    'Score': [85, 90, 90, np.nan]
})
studentseen=[]
keep=[]

for i in range(len(df)):
    student = df.loc[i, 'Student']
    if student not in studentseen:
        studentseen.append(student)
        keep.append(i)

df1 = df.loc[keep].copy()
print(df1)

#activity 4
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X=[[80], [90], [70], [60]]
y=["Pass", "Pass", "Pass", "Fail"]

Xtrain, Xtest, ytrain, ytest=train_test_split(X, y, test_size=0.25, random_state=123)
model=KNeighborsClassifier(n_neighbors=3)
model.fit(Xtrain, ytrain)

newscore=[[75]]
prediction= model.predict(newscore)

print(prediction)