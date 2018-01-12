class Collection:

    def __init__(self, threads):
        self._threads=threads

    @property
    def threads(self):
        return self._threads