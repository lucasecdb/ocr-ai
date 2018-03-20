import pickle

agent = None

print('Carregando o classificador')

with open('./agent_mlp.pkl', 'rb') as file:
    agent = pickle.load(file)

print('DONE.\n')

print('Predizendo os dados de teste e gerando métricas...')

result = agent.test()

print(agent.generate_report())

print('Accuracy: ' + result.astype(str))

print('DONE.\n')
