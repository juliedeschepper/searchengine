class Tokenizer:
    def __init__(self,threads):
        self.threads=threads

    def tokenize(self, threads):
        thread_text_list=[]
        for thread in threads:
            thread_text=""
            thread_text.__add__(thread.relqbody)
            for comment in thread.relCommentList:
                thread_text.__add__(comment.relc_text)
            thread_text_list.append(thread_text)
        
            






