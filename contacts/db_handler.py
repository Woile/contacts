
class CSVDB:
    pass


class DBHandler:
    """"""
    def __init__(self, db=None):
        if db is None:
            db = CSVDB()
        self.db = db

    def load_db_in_memory(self):
        pass

    def save_collection(self):
        pass

    def save(self):
        pass
