from shiva import app
from shiva.tools.db import get_db
from shiva.tools.request import success


@app.route('/')
def index():
    return 'Hello Shiva'


@app.route('/api/v1/track_visit')
def track_visit():
    return success()


@app.route('/api/v1/add_data')
def add_data():
    return success()
