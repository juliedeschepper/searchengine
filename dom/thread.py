class Thread:

    def __init__(self, thread_sequence, subtaska_skip_because_same_as_relquestion_id,relq_id, relq_category, relq_date, relq_userid, relq_username, relqsubject, relqbody,relCommentList):
        self.thread_sequence=thread_sequence
        self.subtaska_skip_because_same_as_relquestion_id=subtaska_skip_because_same_as_relquestion_id
        self.relq_id = relq_id
        self.relq_category = relq_category
        self.relq_date = relq_date
        self.relq_userid = relq_userid
        self.relq_username = relq_username
        self.relqsubject = relqsubject
        self.relqbody = relqbody
        self.relCommentList=relCommentList
