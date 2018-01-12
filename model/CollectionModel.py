from collections import Counter


class CollectionModel:
    def __init__(self, threads):
        self._threads = threads
        self._tfidx = {}
        self.calculate_frequency()

    def calculate_frequency(self):
        words = []
        for thread in self._threads:
            for document in thread._documents:
                for word in document.text:
                    words.append(word)
        wordCount = Counter(words)

        for word, frequency in wordCount.items():
            self._tfidx[word] = frequency / len(words)

        return self._tfidx

    def get_prob_term(self, term):
        return self._tfidx.get(term, 0.00001)
