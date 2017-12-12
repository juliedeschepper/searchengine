from collections import Counter

class Document:
    def __init__(self, words):
        self.words = words

    def frequenties(self):
        freq = Counter(self.words)
        aantal = len(self.words)
        
        return freq

