from collections import Counter

class Document:
    def __init__(self, words):
        self.words = words

    def frequenties(self):
        freq_per_comment = []
        for list in self.words:
            counts = Counter(list)
            aantal = sum(counts.values())
            keys = counts.keys()
            values = counts.values()
            freqvalues = [x / aantal for x in values]
            freqs = dict(zip(keys, freqvalues))
            freq_per_comment.append(freqs)

        return freq_per_comment




