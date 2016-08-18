from flask import Flask, g, jsonify, abort, request
import psycopg2
import settings

app = Flask(__name__)
app.config['DEBUG'] = settings.APP_DEBUG


def get_db():
    if not hasattr(g, 'postgres'):
        conn = psycopg2.connect(
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT)
        g.postgres = conn
    return g.postgres


@app.teardown_appcontext
def close_connection(exception):
    pg = getattr(g, 'postgres', None)
    if pg is not None:
        pg.close()


@app.errorhandler(404)
def not_found(error):
    response = jsonify({'code': 404, 'message': 'Not found'})
    response.status_code = 404
    return response


@app.route('/')
def index():
    return 'Hello Shiva'

if __name__ == '__main__':
    app.run(port=settings.APP_PORT, host=settings.APP_HOST)
