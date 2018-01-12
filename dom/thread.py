class Thread:

    def __init__(self,sequence,query, documents):
        self._sequence = sequence
        self._query = query
        self._documents = documents

    @property
    def sequence(self):
        return self._sequence

    @property
    def query(self):
        return self._query

    @property
    def documents(self):
        return self._documents
