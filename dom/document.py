class Document:

    def __init__(self, id, relevance, text):
        self._id = id
        self._relevance = relevance
        self._text = text

    @property
    def id(self):
        return self._id

    @property
    def relevance(self):
        return self._relevance

    @property
    def text(self):
        return self._text