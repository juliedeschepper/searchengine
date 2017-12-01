import unittest
from dom.reader import Reader


class ReaderTest(unittest.TestCase):
    def testMakeobjectsfromxml(self):
        reader = Reader()
        soup = reader.readfile("../files/testTreadFile.xml")
        reader.makeobjectsfromxml(soup)


if __name__ == '__main__':
    unittest.main()
