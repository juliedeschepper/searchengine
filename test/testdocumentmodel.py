import unittest
from dom.reader import Reader
from dom.tokenization import Tokenizer
from dom.document_model import Document

class DocumentTest(unittest.TestCase):
    def testdocumentmodel(self):
        reader = Reader()
        soup = reader.readfile("../files/testTreadFile.xml")
        threads = reader.makeobjectsfromxml(soup)
        tokenizer = Tokenizer(threads)
        comments_tokenized = tokenizer.tokenize_comments(threads)
        document = Document(comments_tokenized)
        frequenties = document.frequenties()
        print(frequenties)




if __name__ == '__main__':
    unittest.main()
