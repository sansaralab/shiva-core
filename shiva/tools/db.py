import psycopg2
from shiva.common import settings


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
