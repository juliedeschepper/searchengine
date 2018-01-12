from collections import Counter


class DocumentModel:
    def __init__(self, threads):
        self._threads = threads
        self._tfidx = {}
        self.calculate_frequency()

    def calculate_frequency(self):
        for thread in self._threads:
            for document in thread.documents:
                words = document.text
                self._tfidx[document.id] = Counter(words)


    def get_word_doc_prob(self, word, id):
        total_amount = 0
        for key, value in self._tfidx[id].items():
            total_amount += value
        frequency = self._tfidx[id].get(word)
        if frequency is None:
            return 0.0001
        else:
            return frequency / total_amount
