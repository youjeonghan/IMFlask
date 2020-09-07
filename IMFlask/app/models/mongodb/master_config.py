'''
MongoDB master_config Collection Model
'''
from flask import current_app


class MasterConfig:
    '''master_config collection model'''
    def __init__(self, cur):
        self.col = cur[current_app.config['MONGO_DB_NAME']]['master_config']

    def find_all(self):
        '''해당 콜렉션 내에 모든 데이터 반환'''
        return list(
            self.col.find(
                {},
                {"_id": 0}
            )
        )
