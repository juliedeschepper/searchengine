import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from dom.lematizer_stemmer import LemmingStemming


class Tokenizer:
    def __init__(self, threads):
        self.threads = threads
        self.lemmingstemming=LemmingStemming(threads)

    def tokenize(self, threads):
        thread_text_list = []
        for thread in threads:
           thread_text_list.extend(self.tokenize_thread(thread))
        return thread_text_list

    def tokenize_thread(self,thread):
        thread_list=[]
        thread_list.extend(self.eliminate(thread.relqbody))
        for comment in thread.relCommentList:
            array=self.eliminate(comment.relc_text)
            thread_list.extend(array)
        return thread_list

    def tokenize_comments(self,threads):
        thread_text_list = []
        for thread in threads:
            for comment in thread.relCommentList:
                array = self.eliminate(comment.relc_text)
                thread_text_list.extend(array)
        return thread_text_list

    def eliminate(self,text):
        text = text.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        with open( "../files/stopwords_english.txt", encoding="utf8") as f:
            stop_content = f.read()
        tokens_lemmingstemming= [self.lemmingstemming.lemmatizerstemmer(i) for i in tokens]
        remstop = [i for i in tokens_lemmingstemming if i not in stop_content]
        return remstop

            






