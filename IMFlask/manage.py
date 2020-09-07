'''
Flask Application Manage 코드
'''
import os
import unittest
import click
from app import create_app
from app.models import init_app
from app.models.mongodb import get_mongo_cur

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    '''Init shell context'''
    return dict(mongo_cli=get_mongo_cur())


@app.cli.command()
def db_init():
    """First, run the Database init modules."""
    init_app(app)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
