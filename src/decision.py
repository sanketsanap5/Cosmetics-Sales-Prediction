
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree

def preprocess_features(df):
    #Make sure its a dataframe
    df = pd.DataFrame(df,columns=['Age','Income','Gender','Marital Status'])
    df['Age'] = df['Age'].map({'<21':0,'21-35':1,'>35':2}) 
    df['Income'] = df['Income'].map({'Low':0,'Medium':1,'High':2}) 
    df['Gender'] = df['Gender'].map({'Male':0,'Female':1})
    df['Marital Status'] = df['Marital Status'].map({'Single':0,'Married':1})
    print(df.head())
    return df

df = pd.read_csv('C:/Users/Sanket/OneDrive/Documents/BE-II/ML Lab/Assignment Lipstick Prediction/cosmetics.csv')
print('\n\n')
print(df.head())

df.drop(columns=['ID'],inplace= True)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

print("\n\nFeatures :")
print(x.head())
print("\n\Labels :")
print(y.head())

x = preprocess_features(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1,random_state=0)

model = DecisionTreeClassifier(criterion='entropy')
model.fit(x_train,y_train)

print("\n\nAccuracy :",model.score(x_test,y_test))

test = pd.DataFrame({'Age':'<21','Income':'Low','Gender':'Female','Marital Status':'Married'},index=[0])
test = preprocess_features(test)

print("\n\nPrediction for Test Value ",model.predict(test))
tree.export_graphviz(model,out_file='C:/Users/Sanket/OneDrive/Documents/BE-II/ML Lab/Assignment Lipstick Prediction/tree.dot',rounded=True,feature_names=['Age','Income','Gender','Marital Status'],filled=True,class_names=['No','Yes'])
