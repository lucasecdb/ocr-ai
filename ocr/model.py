from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report


class Agent(object):
    '''
    Represents the SVM and MLP agent object
    '''

    def __init__(self, train_data, test_data, train_labels, test_labels, mode='svc'):
        if mode == 'mlp':
            self._svc = MLPClassifier(hidden_layer_sizes = (512), max_iter=900, activation='logistic')
        else:
            self._svc = SVC(C=32, gamma=0.0078125, kernel='poly')
        self._train_data = train_data
        self._train_labels = train_labels
        self._test_data = test_data
        self._test_labels = test_labels

    def train(self):
        self._svc.fit(self._train_data, self._train_labels)

    def test(self):
        return self._svc.score(self._test_data, self._test_labels)

    def generate_report(self):
        predictions = self._svc.predict(self._test_data)

        print(classification_report(self._test_labels, predictions))
