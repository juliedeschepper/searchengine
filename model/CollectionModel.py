from collections import Counter


class CollectionModel:
    def __init__(self, threads):
        self.threads=threads
        self.model = []
        self.initModel()

    def initModel(self):
        words = self.threads.text.split()
        wordCount = Counter(words)

        for word in wordCount:
            self.model[word] = (1 / len(words)) * wordCount[word]

    def prob_term(self,term):
        return 0
