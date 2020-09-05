from app.models.mongodb.master_config import MasterConfig as mongo_MC
from app.models.mysql.master_config import MasterConfig as mysql_MC
from app.models.redis.redis_model import RedisModel


def get_author_with_mongo(mongo_cur):
	model = mongo_MC(mongo_cur)
	data = model.find_all()
	return data


def get_author_with_mysql(mysql_cur):
	model = mysql_MC(mysql_cur)
	data = model.find_all()
	return data


def insert_author_with_mysql(mysql_cur, author):
	model = mysql_MC(mysql_cur)
	model.insert(author)
	model.commit()


def get_author_with_redis():
	model = RedisModel()
	data = model.get_author()
	return data