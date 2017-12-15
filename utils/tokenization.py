from nltk.tokenize import RegexpTokenizer

from utils.lematizer_stemmer import LemmingStemming


class Tokenizer:
    def __init__(self, collection):
        self.collection = collection
        self.lemmingstemming=LemmingStemming(collection)

    def tokenize(self):
        for thread in self.collection.threads:
            thread.query.body=self.tokenizeText(thread.query.body)
            for document in thread.relCommentList:
                document.text=self.tokenizeText(document.text)
        return self.collection

    def tokenizeText(self,text):
        text = text.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        with open( "../files/stopwords_english.txt", encoding="utf8") as f:
            stop_content = f.read()
        tokens_lemmingstemming= [self.lemmingstemming.lemmatizerstemmer(i) for i in tokens]
        remstop = [i for i in tokens_lemmingstemming if i not in stop_content]
        return remstop

            






