from utils.tokenization import Tokenizer

class Document:

    def __init__(self, id,userid,username,relevance2relq, text):
        self.id=id
        self.userid=userid
        self.username=username
        self.relevance2relq=relevance2relq
        self.text=text
        self.tokenizer=Tokenizer(text)

    def get_query_tokenized(self):
        return self.tokenizer.tokenize_query(self.text)