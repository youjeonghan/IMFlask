'''
MySQL User Table Model
'''


class User:
    '''user table'''

    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cur = db_conn.cursor()
        self.table_name = "user"

    def find_all(self):
        '''전체 레코드 조회'''
        sql = "SELECT * FROM {table}"
        sql = sql.format(table=self.table_name) 
        self.cur.execute(sql)
        return self.cur.fetchone()

    def user_id_check(self, user_id):
        '''유저 아이디 유효성 검증'''
        sql = ' SELECT id FROM {table} WHERE id = %s'
        sql = sql.format(table=self.table_name) 
        self.cur.execute(sql, (user_id,))
        return bool(self.cur.fetchone())

    def get_info(self, user_id):
        '''유저 정보 반환'''
        sql = 'SELECT * FROM {table} WHERE id = %s'
        sql = sql.format(table=self.table_name) 
        self.cur.execute(sql, (user_id,))
        return self.cur.fetchone()

    def create_user(self, user_id, user_pw_hash):
        '''유저 데이터 생성'''
        sql = 'INSERT INTO {table}(id, pw) VALUES (%s, %s)'
        sql = sql.format(table=self.table_name)
        self.cur.execute(sql, (user_id, user_pw_hash))

    def commit(self):
        '''디비 갱신 정보 커밋'''
        self.db_conn.commit()

    def rollback(self):
        '''디비 갱신 정보 롤백'''
        self.db_conn.rollback()