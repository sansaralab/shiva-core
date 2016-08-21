from flask import request
from shiva import app
from shiva.tools.request import success, error
from shiva.domain.types import UserData, UserVisit
from .services import insert_user_data, insert_user_visit, run_triggers
from .validators import validate_add_data, validate_track_visit


@app.route('/')
def index():
    return 'Hello Shiva'


@app.route('/api/v1/track_visit', methods=['POST'])
def track_visit():
    visit = UserVisit(
        user_id=request.form.get('user_id', None),
        page=request.form.get('page', None),
        user_agent=request.form.get('user_agent', None),
        ip=request.form.get('ip', None))

    if validate_track_visit(visit):
        insert_user_visit(visit)
        return success()
    else:
        return error()


@app.route('/api/v1/add_data', methods=['POST'])
def add_data():
    """
    action_type - what data we track. now it can be CONTACT, EVENT and DATA.
    action_name - like a key.
    action_value - value of the action.

    Example: (CONTACT, phone, 0123456)

    :return:
    """
    data = UserData(
        user_id=request.form.get('user_id', None),
        action_type=request.form.get('action_type', None),
        action_name=request.form.get('action_name', None),
        action_value=request.form.get('action_value', None))

    if validate_add_data(data):
        insert_user_data(data)
        run_triggers(data)
        return success()
    else:
        return error()
