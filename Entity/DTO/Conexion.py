import pymysql


class Connection:
    def __init__(self, host, port, user, password, db):
        self.database = pymysql.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            db=db
        )

        self.cursor = self.database.cursor()

    def ex_query(self, query):
        self.cursor.execute(query)
        return self.cursor

    def disconnect(self):
        self.database.close()

    def commit(self):
        self.database.commit()

    def rollback(self):
        self.database.rollback()
