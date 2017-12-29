import unittest
from utils.tokenization import Tokenizer
from utils.reader import Reader
from model.CollectionModel import CollectionModel
from model.DocumentModel import DocumentModel


class TestFinal(unittest.TestCase):
    def test_final(self):
        reader = Reader()
        soup = reader.readfile("../files/testTreadFile.xml")
        threads = reader.makeobjectsfromxml(soup)
        tokenizer = Tokenizer(threads)
        collection_tokenized = tokenizer.tokenize()
        coll_model = CollectionModel(collection_tokenized)
        for thread in collection_tokenized.threads:
            for document in thread.relCommentList:
                document_model = DocumentModel(document, coll_model)
                prob_query_document = document_model.prob_document_given_query(thread.query)
                print(thread.thread_sequence)
                print(document.id)
                print(prob_query_document)
                print(document.relevance2relq)
                print("-------------------------------------------")


if __name__ == '__main__':
    unittest.main()
