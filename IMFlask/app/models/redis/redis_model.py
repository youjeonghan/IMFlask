'''
Redis DB Model
'''


class RedisModel:

    def __init__(self, cur):
        self.cur = cur

    def get_author(self):
        return self.cur.get("__author__")
