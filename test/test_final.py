import unittest
from utils.tokenization import Tokenizer
from utils.reader import Reader
from model.CollectionModel import CollectionModel
from model.DocumentModel import DocumentModel
from model.RetrievalModel import RetrievalModel


class TestFinal(unittest.TestCase):
    def test_final(self):
        reader = Reader()
        soup = reader.readfile()
        threads = reader.makeobjectsfromxml(soup)
        tokenizer = Tokenizer(threads)
        collection_tokenized = tokenizer.tokenize()
        coll_model = CollectionModel(collection_tokenized)
        doc_model = DocumentModel(collection_tokenized)
        ret_model = RetrievalModel(collection_tokenized, doc_model, coll_model)
        ret_model.calculate_relevance()


if __name__ == '__main__':
    unittest.main()
