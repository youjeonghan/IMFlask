# IMFlask
**Large Scale Web Backend Structure for Flask**

공부하는 내용을 정리하는 겸, Flask를 사용하여, 대규모 어플리케이션 서버를 구축한다고 가정했을 때의 baseline 코드를 구현한 것입니다. 

여러 오픈 소스를 읽어보고 제 몸에 와닿는 직관적인 부분만 반영한 것이라 부족한 점이 많습니다.

피드백은 적극적으로 환영합니다.

# Concept

### application factory

어플리케이션은 개발(development), 테스팅(Testing), 상용(Production) Level에서 다르게 동작해야 합니다. 따라서 실행하고자 하는 환경에 따라 config를 다르게 주입시키는 애플리케이션 팩토리를 구현했습니다.



### 가능한 한 Flask Extension을 지양하자

Flask extension는 유용하지만 몇가지 문제가 있다고 생각했습니다.

- 몇몇 extension은 업데이트가 되지 않고 있습니다. 대표적으로 많은 Flask open source에서 사용하고 있는 **flask_script**가 그렇습니다. 

- 확실히 쓰면 편리하지만, 몇몇 package는 오히려 자체의 rule을 강요받는다는 느낌이 들었습니다.
  저의 생각과 일치하거나, 제가 직접 구현이 불가능한 수준이 아니라면 굳이 확장 패키지**(flask_moment)**를 사용하지 않았습니다.

따라서 Flask 및 Python 자체에서 기본적으로 지원하는 기능을 충실히 활용하도록 노력했습니다.



### 가능한 한 저수준의 드라이버를 사용하자

해당 코드는 RDBMS, NoSQL(Document based, Key-value based) 등의 **총 3가지의 DB(MySQL, MongoDB, Redis)**와 연동한 예제 코드가 작성되어 있습니다. 

모든 DB단 연동 코드에는 **ORM, ODM과 같은 Database Abstraction Module을 사용하지 않았습니다.**

당연히 Large Scale이라면, Abstraction을 사용하는게 보편적이지만, 저는 공부하는 입장에서 제가 직접 DB까지 전달되는 처리를 가능한 한 자세하게 관여할 수 있도록 구조를 구현하였습니다.



### view 함수가 비대해지는 것을 최대한 막자





# Required Environment variable

- FLASK_SECRET_KEY
- FLASK_TEST_ACCESS_TOKEN

- FLASK_MYSQL_URI

- FLASK_MONGO_URI
- FLASK_MONGO_DB_NAME 

- FLASK_REDIS_HOST
- FLASK_REDIS_PW

- FLASK_CONFIG
- FLASK_ENV
- FLASK_APP


# Directories
```
/
.git/
.gitignore
requirements.txt
LICENSE
README.md

IMFlask/
	manage.py
	config.py
	
	tests/
		__init__.py
		*test_framework.py

	modules/
		__init__.py
		*ext_module.py
	
	app/
		__init__.py
		decorator.py
		
		client/
			*front-end/
		
		templates/
			*.html
		
		static/
			*static_files
		
		models/
			__init__.py
			/mysql
				__init__.py
				db.py
				*models.py
			/mongo
				__init__.py
				db.py
				*model.py
			/redis
				__init__.py
				db.py
				*model.py
		
		controllers/
				__init__.py
				*controller.py
		
		api/
			__init__.py		
			v1/
				__init__.py
				*api.py
			auth/
				__init__.py
				*auth_api.py
			
			
		

```

# References
https://github.com/JoMingyu/Flask-Large-Application-Example

https://github.com/miguelgrinberg/flasky