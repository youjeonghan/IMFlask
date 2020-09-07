'''
Redis DB Model
'''

class RedisModel:
    '''redis model'''
    def __init__(self, cur):
        self.cur = cur

    def get_author(self):
        '''author value 반환'''
        return self.cur.get("__author__")
