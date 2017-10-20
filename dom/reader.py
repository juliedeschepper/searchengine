from bs4 import BeautifulSoup


class Reader:
    def __init__(self):
        self.file1 = "files/SemEval2016-Task3-CQA-QL-dev-subtaskA.xml"
        self.file2 = "files/SemEval2016-Task3-CQA-QL-train-part1-subtaskA.xml"
        self.file3 = "files/SemEval2016-Task3-CQA-QL-train-part2-subtaskA.xml"

    def readfile(self,file):
        fileToRead = open(file, encoding="utf8")
        content = fileToRead.read()
        soup = BeautifulSoup(content, "lxml")
        return soup

    def makeObjectsFromXML(self,soup):
        threads=soup.findAll('thread')
        for thread in threads:
            thread_attrs = dict(thread.attrs)
            thread_sequence = thread_attrs[u'thread_sequence']



    def getfile1(self):
        return self.file1

    def getfile2(self):
        return self.file2

    def getfile3(self):
        return self.file3



