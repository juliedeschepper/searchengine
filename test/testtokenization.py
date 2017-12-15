import unittest

from dom.tokenization import Tokenizer
from dom.document_model import Document

from utils.reader import Reader


class TokenizerTest(unittest.TestCase):
    def testtokenizerfromfile(self):
        reader = Reader()
        soup = reader.readfile("../files/testTreadFile.xml")
        threads = reader.makeobjectsfromxml(soup)
        tokenizer = Tokenizer(threads)
        threads_tokenized = tokenizer.tokenize(threads)
        print(threads_tokenized)


if __name__ == '__main__':
    unittest.main()
