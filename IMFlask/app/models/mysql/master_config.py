'''
MySQL master_config Collection Model
'''


class MasterConfig:
    '''master config table'''
    
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cur = db_conn.cursor()
        self.table_name = "master_config"

    def find_all(self):
        '''전체 레코드 조회'''
        sql = "SELECT * FROM {table}"
        sql = sql.format(table=self.table_name)
        self.cur.execute(sql)
        return self.cur.fetchone()

    def insert(self, auhtor):
        '''레코드 삽입'''
        sql = "INSERT INTO {table}(author) VALUES (%s);"
        sql = sql.format(table=self.table_name)
        self.cur.execute(sql, (auhtor,))

    def commit(self):
        '''디비 갱신 정보 커밋'''
        self.db_conn.commit()

    def rollback(self):
        '''디비 갱신 정보 롤백'''
        self.db_conn.rollback()
