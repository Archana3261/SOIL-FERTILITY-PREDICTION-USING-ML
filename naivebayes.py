import sys
import numpy as np
import csv
from os.path import dirname, exists, expanduser, isdir, join, splitext
import os 
# Gaussian Naive Bayes

from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

map = {1: "Very Low",2: "low",3: "Moderate",4: "Moderate High",5: "High",6: "Very High"}

def load_file(cwd, data_file_name):
    with open(join(cwd, data_file_name)) as csv_file:
      return load_fileStream(csv_file)

def load_fileStream(fileStream):
    reader = csv.reader(fileStream)
    temp = next(reader)
    n_samples = int(temp[0])
    n_features = int(temp[1])
    temp = next(reader)
    data = np.empty((n_samples, n_features))
    labels = np.empty((n_samples,), dtype=np.int64)

    for i, ir in enumerate(reader):
        data[i] = np.asarray(ir[:-1], dtype=np.float64)
        labels[i] = np.asarray(ir[-1], dtype=np.int64)

    return data, labels


#current working directory
cwd = os.getcwd()

# load the trained datasets 
data, target_labels = load_file(cwd, 'upload/trained_soil_data.csv')

# fit a Naive Bayes model to the data
model = GaussianNB()
model.fit(data, target_labels)

def analyze(fileStream):
    test_data, test_labels = load_fileStream(fileStream)

    # make predictions
    predicted = model.predict(test_data)
    return map[predicted[0]]
