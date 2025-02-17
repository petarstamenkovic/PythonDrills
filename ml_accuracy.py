# Simple Python introduction to ML 

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import joblib

music_data = pd.read_csv('music.csv')               # Loading data into a object

# Manual separtation of a training and test sets
X = music_data.drop(columns=['genre'])              # X is a training set
y = music_data['genre']                             # y is a test set

# Automatic separation of a training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # Allocating 20% of data for testing

model = DecisionTreeClassifier()
model.fit(X_train,y_train)                          # This function does a model training

# joblib.dump(model, 'music-recommender.joblib')    # This is a way to save a trained model for another usage later
# model = joblib.load('music-recommender.joblib')   # This is a way to load a saved model

predictions = model.predict(X_test)                 # This is a general way of using predictions
# predictions = model.predict([ [21, 1] ])          # This is a specific prediction, 21 year old male

score = accuracy_score(y_test, predictions)         # This is a function that calculates the accuracy of a ML model

# Function that draws out a graphic representaion of a decision tree

# tree.export_graphviz(model, out_file='music-recommender.dot',
#                      feature_names=['age', 'gender'],
#                      class_names=sorted(y.unique()), # Class of a node
#                      label='all',
#                      rounded=True,
#                      filled=True) 

