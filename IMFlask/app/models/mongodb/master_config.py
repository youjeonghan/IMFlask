'''
MongoDB master_config Collection Model
'''
from flask import current_app


class MasterConfig:
	def __init__(self, cur):
		self.col = cur[current_app.config['MONGO_DB_NAME']]['master_config']

	def find_all(self):
		return list(
			self.col.find(
				{},
				{"_id": 0}
			)
		)