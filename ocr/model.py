from sklearn.svm import SVC


class Agent(object):
    '''
    Represents the SVM agent object
    '''

    def __init__(self, train_data, test_data, train_labels, test_labels):
        self._svc = SVC(C=32, gamma=0.0078125)
        self._train_data = train_data
        self._train_labels = train_labels
        self._test_data = test_data
        self._test_labels = test_labels

    def train(self):
        self._svc.fit(self._train_data, self._train_labels)

    def test(self):
        return self._svc.score(test_data, test_labels)

    def generate_report(self):
        predictions = self._svc.predict(test_data)

        print(classification_report(test_labels, predictions))
