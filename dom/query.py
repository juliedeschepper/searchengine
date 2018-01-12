class Query:

    def __init__(self,id, subject, body ):
        self._id = id
        self._subject = subject
        self._body = body

    @property
    def id(self):
        return self._id

    @property
    def subject(self):
        return self._subject

    @property
    def body(self):
        return self._body

