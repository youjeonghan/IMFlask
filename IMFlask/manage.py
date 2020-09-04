import os
import click
import unittest
from app import create_app
from app.models.mongo.db import get_cursor

app = create_app(os.getenv('FLASK_CONFIG', 'default'))


@app.shell_context_processor
def make_shell_context():
	return dict(mongo_cli=get_cursor())


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
	"""Run the unit tests."""
	if test_names:
		tests = unittest.TestLoader().loadTestsFromNames(test_names)
	else:
		tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)