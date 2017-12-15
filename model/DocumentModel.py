from collections import Counter


class DocumentModel:
    def __init__(self, document):
        self.document = document
        self.model = []
        self.initModel()

    def initModel(self):
        words = self.document.text.split()
        wordCount = Counter(words)

        for word in wordCount:
            self.model[word] = (1 / len(words)) * wordCount[word]


    def prob_document_given_query(self,query):
        return 0