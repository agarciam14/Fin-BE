from datetime import datetime
import uuid

from project import db

def save_passive(passive):
    message = {'type': '', 'message': ''}
    try:
        passive_to_save = {
            '_id': str(uuid.uuid1()),
            'user': passive['user'],
            'amount': passive['amount'],
            'currency': passive['currency'],
            'type': passive['type'],
            'status': passive['status'],
            'limit_date': passive['limit_date'],
            'created_at': datetime.isoformat(datetime.now()),
            'updated_at': datetime.isoformat(datetime.now()),
        }
        db.passive.insert_one(passive_to_save)
        message["type"] = "True"
        message["message"] = passive_to_save
    except Exception as ex:
        message["type"] = "False"
        message["message"] = ex
        print(ex)
    return message

def list_passives(user):
    message = {'type': '', 'message': ''}
    try:
        passives = list(db.passive.find({'user': user}))
        message['type'] = 'True'
        message['message'] = passives
    except Exception as ex:
        message['type'] = 'False'
        message['message'] = ex
    return message

