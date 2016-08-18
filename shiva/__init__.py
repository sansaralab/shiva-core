from flask import Flask, g
from shiva.tools.request import error
app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    pg = getattr(g, 'postgres', None)
    if pg is not None:
        pg.close()


@app.errorhandler(404)
def not_found(err):
    return error({'message': 'Not found'})


import shiva.tracker.views
