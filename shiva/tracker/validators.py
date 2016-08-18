def validate_add_data(data):
    for item in data.values():
        if item is None:
            return False
    return True


def validate_track_visit(data):
    for item in data.values():
        if item is None:
            return False
    return True
