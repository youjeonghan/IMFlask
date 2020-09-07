'''
WSGI Application 전용 코드
'''
from manage import app as application

if __name__ == "__main__":
    application.run()
