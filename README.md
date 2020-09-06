# IMFlask
Large Scale Web Backend Structure for Flask

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
https://github.com/miguelgrinberg/flasky
