'''
MongoDB master_config Collection Model
'''
from flask import current_app


class User:
	def __init__(self, cur):
		self.col = cur[current_app.config['MONGO_DB_NAME']]['user']

	def validate(self, user_id):
		return bool(
			self.col.find_one(
				{"user_id": user_id},
				{"_id": 0}
			)
		)

	def get_info(self, user_id):
		return list(
			self.col.find_one(
				{"user_id": user_id},
				{"_id": 0}
			)
		)