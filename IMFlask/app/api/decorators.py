'''
API Main Decorator
'''
from flask import current_app
from time import time


def timer(f):
    def wrapper(*args, **kwargs):
        if not current_app.config['DEBUG']:
            return f(*args, **kwargs)
        process_time = time()
        result = f(*args, **kwargs)
        process_time = time() - process_time
        result['process_time'] = process_time
        return result
    return wrapper