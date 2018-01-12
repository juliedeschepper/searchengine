from collections import OrderedDict
from collections import defaultdict

class RetrievalModel:
    def __init__(self, threads, documentmodel, collectionmodel):
        self._collection_model = collectionmodel
        self._document_model = documentmodel
        # self._query_model = querymodel
        self._threads = threads
        self._lambda = 0.5


    def calculate_relevance(self):
        for thread in self._threads:
            thread_relevancy = {}
            query_words = thread.query.subject + thread.query.body
            for document in thread.documents:
                # query_words = self._query_model.get_query_words(comment.relc_id)
                relevancy_document = 0
                user_relevancy = "true" if document.relevance == "Good" else "false"
                for word in query_words:
                    coll_prob = self._collection_model.get_prob_term(word)
                    doc_prob = self._document_model.get_word_doc_prob(word,document.id)
                    relevancy_word = (1 - self._lambda) * coll_prob + self._lambda * doc_prob
                    relevancy_document += relevancy_word
                thread_relevancy[document.id] = [thread.sequence, document.id, relevancy_document, user_relevancy]
            self.print_ranked_comments(thread_relevancy, thread)

    def print_ranked_comments(self, thread_relevancy, thread):
        ordered_thread_relevancy = OrderedDict(sorted(thread_relevancy.items(), key=lambda t: t[1][2], reverse=True))
        count = 1
        ranked_threads = defaultdict(list)
        for key, value in ordered_thread_relevancy.items():
            ranked_threads[count] = value
            count += 1
        for document in thread.documents:
            for ordered_key, ordered_value in ranked_threads.items():
                if document.id == ordered_value[1]:
                    out = str(ordered_value[0])+'\t'+ str(ordered_value[1])+'\t'+ str(ordered_key) +'\t'+ str(ordered_value[2])+'\t'+ str(ordered_value[3])+'\n'
                    self.write_to_file(out)

    def write_to_file(self, document):
        with open('out.txt', 'a') as f:
            f.write(document)
