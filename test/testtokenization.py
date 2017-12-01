import unittest
from dom.reader import Reader
from dom.tokenization import Tokenizer



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
