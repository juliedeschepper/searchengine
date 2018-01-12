import unittest

from utils.tokenization import Tokenizer

from utils.reader import Reader


class TokenizerTest(unittest.TestCase):
    def testtokenizerfromfile(self):
        reader = Reader()
        soup = reader.readfile()
        threads = reader.makeobjectsfromxml(soup)
        tokenizer = Tokenizer(threads)
        threads_tokenized = tokenizer.tokenize()
        for thread in threads_tokenized:
            print(thread._query._body)
            for document in thread._documents:
                print(document._text)


if __name__ == '__main__':
    unittest.main()
