from bs4 import BeautifulSoup
from dom.thread import Thread
from dom.collection import Collection
from dom.query import Query
from dom.document import Document

from pprint import pprint


class Reader:
    def __init__(self):
        self._file1 = "../files/SemEval2016-Task3-CQA-QL-dev-subtaskA.xml"
        # self.file2 = "files/SemEval2016-Task3-CQA-QL-train-part1-subtaskA.xml"
        # self.file3 = "files/SemEval2016-Task3-CQA-QL-train-part2-subtaskA.xml"

    def readfile(self):
        with open(self._file1, encoding="utf8") as f:
         content = f.read()
        soup = BeautifulSoup(content, "xml")
        return soup

    def makeobjectsfromxml(self,soup):
        thread_list = []
        for thread in soup.findAll('Thread'):
            query = thread.RelQuestion
            query_object = Query(query.get('RELQ_ID'),
                              query.RelQSubject.get_text(strip=True),
                                 query.RelQBody.get_text(strip=True))
            document_list = []
            for comment in thread.findAll('RelComment'):
                document_object = Document(comment.get('RELC_ID'),
                                           comment.get('RELC_RELEVANCE2RELQ'),
                                           comment.RelCText.get_text(strip=True))
                document_list.append(document_object)

            thread_object = Thread(thread.get('THREAD_SEQUENCE'),
                                   query_object,
                                   document_list)
            thread_list.append(thread_object)
        return thread_list

