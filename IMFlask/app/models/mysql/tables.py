'''
Mysql Table Create Queries
'''
tables = [
# master_config Table
'''
    CREATE TABLE IF NOT EXISTS master_config (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        author VARCHAR(20) NOT NULL,
        PRIMARY KEY(id)
    );
''',
'''
    CREATE TABLE IF NOT EXISTS user (
        id VARCHAR(200) NOT NULL,
        pw VARCHAR(200) NOT NULL,
        PRIMARY KEY(id)
    );
''',
]
