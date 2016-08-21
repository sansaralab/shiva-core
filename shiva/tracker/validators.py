from shiva.domain.types import UserVisit, UserData


def validate_add_data(data: UserData):
    for item in data:
        if item is None:
            return False
    return True


def validate_track_visit(data: UserVisit):
    for item in data:
        if item is None:
            return False
    return True
