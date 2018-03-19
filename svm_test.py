import pickle

agent = None

print('Carregando o classificador')

with open('./agent.pkl', 'rb') as file:
    agent = pickle.load(file)

print('DONE.\n')

print('Testando o classificador')

print(agent.test())
print(agent.generate_report())

print('DONE.\n')
