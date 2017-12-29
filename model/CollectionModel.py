from collections import Counter


class CollectionModel:
    def __init__(self, collection):
        self.threads = collection.threads
        self.tfidx =  {}
        self.initModel()

    def initModel(self):
        words=[]
        for thread in self.threads:
            for document in thread.relCommentList:
                for word in document.text:
                    words.append(word)
        wordCount = Counter(words)
        for word in wordCount:
            self.tfidx[word] = (1 / len(words)) * wordCount[word]
        return self.tfidx


    def prob_term(self, term):
        for key, value in self.tfidx.items():
            if key == term:
                return value
        return 0
