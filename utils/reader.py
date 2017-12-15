from bs4 import BeautifulSoup
from dom.thread import Thread
from pprint import pprint


class Reader:
    def __init__(self):
        self.file1 = "files/SemEval2016-Task3-CQA-QL-dev-subtaskA.xml"
        self.file2 = "files/SemEval2016-Task3-CQA-QL-train-part1-subtaskA.xml"
        self.file3 = "files/SemEval2016-Task3-CQA-QL-train-part2-subtaskA.xml"

    def readfile(self,file):
        with open(file, encoding="utf8") as f:
         content = f.read()
        soup = BeautifulSoup(content, "lxml")
        return soup

    def makeobjectsfromxml(self,soup):
        thread_list=[]
        threads=soup.findAll('thread')
        for thread in threads:
            thread_attrs = dict(thread.attrs)
            thread_sequence = thread_attrs[u'thread_sequence']
            relQuestion=thread.find('relquestion')
            relQuestion_attrs=dict(relQuestion.attrs)
            relq_id=relQuestion_attrs[u'relq_id']
            relq_subcategory = relQuestion_attrs[u'relq_category']
            relq_date = relQuestion_attrs[u'relq_date']
            relq_userid = relQuestion_attrs[u'relq_userid']
            relq_username = relQuestion_attrs[u'relq_username']
            relq_relqsubject = relQuestion.find('relqsubject').get_text(strip=True)
            relq_body = relQuestion.find('relqbody').get_text(strip=True)
            relq_relcommentlist =[]
            for comment in thread.findAll('relcomment'):
                comment_attrs = dict(comment.attrs)
                relc_id = comment_attrs[u'relc_id']
                relc_userid = comment_attrs[u'relc_userid']
                relc_username = comment_attrs[u'relc_username']
                relc_relevance2relq = comment_attrs[u'relc_relevance2relq']
                relc_text= comment.find('relctext').get_text(strip=True)
                relComment=RelComment(relc_id,relc_userid,relc_username,relc_relevance2relq,relc_text)
                relq_relcommentlist.append(relComment)
            t = Thread(thread_sequence, relq_id, relq_subcategory, relq_date, relq_userid, relq_username,
                       relq_relqsubject, relq_body, relq_relcommentlist)
            thread_list.append(t)
        return thread_list

    def printobjects(self,list):
        for t in list:
            print(t.thread_sequence)
        print(len(list))

    def getfile1(self):
        return self.file1

    def getfile2(self):
        return self.file2

    def getfile3(self):
        return self.file3



