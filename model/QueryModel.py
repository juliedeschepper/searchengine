from collections import defaultdict


class QueryModel:
    def __init__(self, threads):
        self._threads = threads
        self._words_per_query = defaultdict(list)
        self.fill_dict()

    def fill_dict(self):
        for thread in self._threads:
            for document in thread._documents:
                for word in document.text:
                    self._words_per_query[thread.relq_id].append(word)

    def get_query_words(self, thread_id):
        return self._words_per_query.get(thread_id)
