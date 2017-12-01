from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

class LemmingStemming:
    def __init__(self, threads):
        self.threads=threads

    def lemmatizerstemmer(self,word):
        word_lemmatized=self.lemmatizer(word)
        word_stemmed=self.stemmer(word)
        return word_stemmed

    def lemmatizer(self, word):
        wordnet_lemmatizer = WordNetLemmatizer()
        word_lemmatized = wordnet_lemmatizer.lemmatize(word)
        return word_lemmatized

    def stemmer(self,word):
        porter_stemmer = PorterStemmer()
        word_stemmed=porter_stemmer.stem(word)
        return word_stemmed

