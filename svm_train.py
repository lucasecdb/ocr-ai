import pickle

from ocr.model import Agent
from ocr.utils import get_dataset
from sklearn.model_selection import train_test_split

data_labels = []
hog_features = []

print('Efetuando a leitura dos dados e tratando imagens...')

data, data_labels = get_dataset('./data/normalized')

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
