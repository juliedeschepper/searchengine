from nltk.tokenize import RegexpTokenizer
from utils.lematizer_stemmer import LemmingStemming


class Tokenizer:
    def __init__(self, threads):
        self._threads = threads
        self._lemmingstemming = LemmingStemming(threads)

    def tokenize(self):
        for thread in self._threads:
            thread._query._subject = self.tokenize_text(thread._query._subject)
            thread._query._body = self.tokenize_text(thread._query._body)
            for document in thread._documents:
                document._text = self.tokenize_text(document._text)
        return self._threads

    def tokenize_text(self,text):
        text = text.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        with open( "../files/stopwords_english.txt", encoding="utf8") as f:
            stop_content = f.read()
        tokens_lemmingstemming= [self._lemmingstemming.lemmatizerstemmer(i) for i in tokens]
        remstop = [i for i in tokens_lemmingstemming if i not in stop_content]
        return remstop

            






