from collections import Counter

class Document:
    def __init__(self, words):
        self.words = words

    def frequenties(self):
        counts = Counter(self.words)
        aantal = sum(counts.values())
        keys = counts.keys()
        values = counts.values()
        freqvalues = [x / aantal for x in values]
        freqs = dict(zip(keys,freqvalues))

        return freqs

