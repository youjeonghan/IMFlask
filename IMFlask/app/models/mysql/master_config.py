'''
MongoDB master_config Collection Model
'''


class MasterConfig:
	
	def __init__(self, db_conn):
		self.db_conn = db_conn
		self.cur = db_conn.cursor()
		self.table_name = "master_config" 

	def find_all(self):
		sql = "SELECT * FROM " + self.table_name
		self.cur.execute(sql)
		return self.cur.fetchone()

	def insert(self, auhtor):
		sql = "INSERT INTO imltable(author) VALUES (%s);"
		self.cur.execute(sql, (auhtor,))

	def commit(self):
		self.db_conn.commit()

	def rollback(self):
		self.db_conn.rollback()