import unittest
from utils.reader import Reader
from utils.tokenization import Tokenizer
from model.DocumentModel import DocumentModel
from model.CollectionModel import CollectionModel


class DocumentTest(unittest.TestCase):


    def testdocumentmodel(self):
        reader = Reader()
        soup = reader.readfile("../files/testTreadFile.xml")
        collection = reader.makeobjectsfromxml(soup)
        tokenizer = Tokenizer(collection)
        collection_tokenized = tokenizer.tokenize()
        for thread in collection_tokenized.threads:
            print(thread.query.body)
            for document in thread.relCommentList:
                print(document.text)
                document_model = DocumentModel(document.text)
                tfidx = document_model.tfidx_document()
                print(tfidx)





if __name__ == '__main__':
    unittest.main()
