from collections import Counter


class DocumentModel:
    def __init__(self, document):
        self.document = document
        self.tfidx = []

    def tfidx_document(self):
        counts = Counter(self.document)
        print(counts)
        aantal = sum(counts.values())
        keys = counts.keys()
        values = counts.values()
        freqvalues = [x / aantal for x in values]
        freqs = dict(zip(keys, freqvalues))
        self.tfidx.append(freqs)

        return self.tfidx


    def prob_document_given_query(self,query):
        return 0