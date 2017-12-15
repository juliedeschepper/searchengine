from collections import Counter


class DocumentModel:
    def __init__(self, document):
        self.document = document
        self.model = []
        self.initModel()

    def initModel(self):
        tfidx = []
        for list in self.words:
            counts = Counter(list)
            aantal = sum(counts.values())
            keys = counts.keys()
            values = counts.values()
            freqvalues = [x / aantal for x in values]
            freqs = dict(zip(keys, freqvalues))
            tfidx.append(freqs)

        return tfidx


    def prob_document_given_query(self,query):
        return 0