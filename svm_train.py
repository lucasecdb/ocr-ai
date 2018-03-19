import os
import re
import pickle
import numpy as np

from ocr.model import Agent
from skimage.io import imread
from skimage.feature import hog
from sklearn.model_selection import train_test_split

data_labels = []
hog_features = []

print('Efetuando a leitura dos dados...')

for path, dir, files in os.walk('./data/normalized'):
    for file in files:
        label = re.search('0+(.+?)-', file)
        features = hog(image=imread(os.path.join(path, file)), orientations=8,
                       block_norm='L2', pixels_per_cell=(4, 4), cells_per_block=(2, 2))
        hog_features.append(features)
        if label:
            data_labels.append(label.group(1))

data = np.array(hog_features)

train_data, test_data, train_labels, test_labels = train_test_split(
    data, data_labels, test_size=0.2, random_state=0)

print('DONE.\n')

print('Treinando e salvando o classificador SVC...')

agent = Agent(train_data, test_data, train_labels, test_labels)
agent.train()

with open('./agent.pkl', 'wb') as file:
    pickle.dump(agent, file)

print('DONE.\n')
