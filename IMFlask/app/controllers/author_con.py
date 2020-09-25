'''
Author Controller
'''
from app.models.mysql.master_config import MasterConfig


def get_author(mysql_cur):
    '''get_author_with_mysql con'''
    model = MasterConfig(mysql_cur)
    data = model.find_all()
    return data


def insert_author(mysql_cur, author):
    '''put_author_with_mysql con'''
    model = MasterConfig(mysql_cur)
    model.insert(author)
    model.commit()

