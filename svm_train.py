import os
import re
import pickle
import numpy as np

from ocr.model import Agent
from skimage.io import imread
from skimage.feature import hog
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from matplotlib import interactive

interactive(True)

data_labels = []
hog_features = []

print('Efetuando a leitura dos dados e tratando imagens...')

for path, dir, files in os.walk('./data/normalized'):
    for file in files:
        label = re.search('0+(.+?)-', file)
        features = hog(image=imread(os.path.join(path, file)), orientations=4,
                       block_norm='L2', pixels_per_cell=(4, 4), cells_per_block=(2, 2))
        # Descomente para plotar as imagens
        # features, hog_image = hog(image=imread(os.path.join(path, file)),orientations=4, block_norm='L2', pixels_per_cell=(4, 4), cells_per_block=(2,2), visualise=True)
        # plt.imshow(imread(os.path.join(path, file)))
        # input('Plotando imagem original normalizada e em escala de cinza')
        # plt.imshow(hog_image)
        # input('Plotando imagem de histogramas de gradientes orientados')
        hog_features.append(features)
        if label:
            data_labels.append(label.group(1))

data = np.array(hog_features)
print('DONE.\n')

print('Repartindo os dados em dados de treino e dados de teste 70/30')
train_data, test_data, train_labels, test_labels = train_test_split(
    data, data_labels, test_size=0.3, random_state=0)
print('DONE.\n')

print('Treinando e salvando o classificador SVC...')

agent = Agent(train_data, test_data, train_labels, test_labels)
agent.train()

with open('./agent.pkl', 'wb') as file:
    pickle.dump(agent, file)

print('DONE.\n')
