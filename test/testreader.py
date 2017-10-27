import unittest
from hamcrest import *
from dom.reader import Reader


class ReaderTest(unittest.TestCase):
    def testMakeobjectsfromxml(self):
        reader = Reader()
        soup = reader.readfile("../files/SemEval2016-Task3-CQA-QL-dev-subtaskA.xml")
        reader.makeobjectsfromxml(soup)

if __name__ == '__main__':
    unittest.main()