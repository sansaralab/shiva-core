from shiva.tools.db import get_db
from shiva.domain.types import UserData, UserVisit


def insert_user_data(data: UserData):
    conn = get_db()
    with conn.cursor() as cur:
        query = 'INSERT INTO user_data (user_id, action_type, action_name, action_value) VALUES (%s, %s, %s, %s)'
        args = (data.user_id, data.action_type, data.action_name, data.action_value)
        cur.execute(query, args)
        conn.commit()
        return True


def insert_user_visit(data: UserVisit):
    conn = get_db()
    with conn.cursor() as cur:
        query = 'INSERT INTO user_visits (user_id, page, useragent, ip) VALUES (%s, %s, %s, %s)'
        args = (data.user_id, data.page, data.user_agent, data.ip)
        cur.execute(query, args)
        conn.commit()
        return True


def insert_trigger():
    pass


def run_triggers(data):
    return True
