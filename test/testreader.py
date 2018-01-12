import unittest

from utils.reader import Reader


class ReaderTest(unittest.TestCase):
    def testMakeobjectsfromxml(self):
        reader = Reader()
        soup = reader.readfile()
        threads = reader.makeobjectsfromxml(soup)
        for thread in threads:
            for document in thread._documents:
                print(document.text)


if __name__ == '__main__':
    unittest.main()
