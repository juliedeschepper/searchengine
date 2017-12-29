from collections import Counter


class DocumentModel:
    def __init__(self, document, collectionmodel):
        self.document = document
        self.tfidx = {}
        self.initModel()
        self.collectionmodel = collectionmodel

    def initModel(self):
        words = self.document.text
        wordCount = Counter(words)

        for word in wordCount:
            self.tfidx[word] = (1 / len(words)) * wordCount[word]


    def prob_document_given_query(self, query):
        if self.document.__sizeof__() == 0:
            return 0
        prob_query_document = 1
        for word in query.body:
            for key, value in self.tfidx.items():
                if key == word:
                    prob_word_everywhere = 0.5 * value + (1 - 0.5) * self.collectionmodel.prob_term(word)
                    prob_query_document = prob_query_document * prob_word_everywhere
                else:
                    prob_word_everywhere = 0.5 * 0 + (1 - 0.5) * self.collectionmodel.prob_term(word)
                    prob_query_document = prob_query_document * prob_word_everywhere
        return prob_query_document
