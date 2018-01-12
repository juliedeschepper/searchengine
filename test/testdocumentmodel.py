import unittest
from utils.reader import Reader
from utils.tokenization import Tokenizer
from model.DocumentModel import DocumentModel
from model.CollectionModel import CollectionModel


class DocumentTest(unittest.TestCase):


    def testdocumentmodel(self):
        reader = Reader()
        soup = reader.readfile()
        threads = reader.makeobjectsfromxml(soup)
        tokenizer = Tokenizer(threads)
        threads_tokenized = tokenizer.tokenize()
        collection_model = CollectionModel(threads_tokenized)
        freq_collection = collection_model.calculate_frequency()
        print(freq_collection)
        document_model = DocumentModel(threads_tokenized)
        freq_document = document_model.calculate_frequency()
        print(freq_document)













if __name__ == '__main__':
    unittest.main()
