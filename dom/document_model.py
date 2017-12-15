from collections import Counter

class Document:
    def __init__(self, words):
        self.words = words

    def frequenties(self):
        for list in self.words:
            counts = Counter(list)
            aantal = sum(counts.values())
            keys = counts.keys()
            values = counts.values()
            freqvalues = [x / aantal for x in values]
            freqs = dict(zip(keys, freqvalues))
            print(freqs)




