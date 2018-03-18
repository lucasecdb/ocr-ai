import os
import re

from skimage.io import imread
from skimage.feature import hog
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV

from sklearn import svm

import numpy as np

import scipy

###### Leitura dos dados de treino e respectivas labels ######

hog_images = []
data_labels = []
hog_features = []

print('Efetuando a leitura dos dados...')

for path, dir, files in os.walk('./data/normalized'):
    for file in files:
        label = re.search('0+(.+?)-', file)
        # image = imread(os.path.join(path, file))
        features = hog(image=imread(os.path.join(path, file)),orientations=8, block_norm='L2', pixels_per_cell=(4, 4), cells_per_block=(2,2))
        # hog_images.append(image)
        hog_features.append(features)
        if label:
        	data_labels.append(label.group(1))

# hog_features = np.array(hog_features)
data = np.array(hog_features)
# data = data.reshape(len(data), -1)


train_data, test_data, train_labels, test_labels = train_test_split(data, data_labels, test_size=0.6, random_state=0)

print('DONE.\n')

print('Treinando o classificador SVC...')

svc = svm.SVC(C=32, gamma=0.0078125)
# parameters = {'C': scipy.stats.expon(scale=100), 'gamma': scipy.stats.expon(scale=.1),'kernel': ['rbf', 'linear']}
# agent = RandomizedSearchCV(svc, parameters)
agent = svc.fit(train_data, train_labels)

print('DONE.\n')

print('Predizendo os dados de teste...')

result = agent.score(test_data, test_labels)
print(result)

print('FIM.')
