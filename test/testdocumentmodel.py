import unittest
from utils.reader import Reader
from utils.tokenization import Tokenizer
from model.DocumentModel import DocumentModel

class DocumentTest(unittest.TestCase):
    def testdocumentmodel(self):
        reader = Reader()
        soup = reader.readfile("../files/testTreadFile.xml")
        threads = reader.makeobjectsfromxml(soup)
        tokenizer = Tokenizer(threads)
        comments_tokenized = tokenizer.tokenize_comments(threads)
        print(comments_tokenized)
        document = DocumentModel(comments_tokenized)
        print(document)




if __name__ == '__main__':
    unittest.main()
