from app.api.v1 import api_v1 as api


@api.route('/author/mysql', methods=['GET', 'PUT'])
def apiv1_get_author_with_mysql():
	pass

@api.route('/author/mongodb')
def apiv1_get_author_with_mongodb():
	pass

@api.route('/author/redis')
def apiv1_get_author_with_redis():
	pass