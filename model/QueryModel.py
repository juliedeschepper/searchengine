from collections import Counter


class QueryModel:
    def __init__(self, query):
        self.query = query
        self.model = []
        self.initModel()

    def initModel(self):
        words = self.query.text.split()
        wordCount = Counter(words)

        for word in wordCount:
            self.model[word] = (1 / len(words)) * wordCount[word]