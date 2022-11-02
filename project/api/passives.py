import json
from flask import Blueprint, request, jsonify

from project.model import passives as passive_model

passives_app = Blueprint('passives_app', __name__)

@passives_app.route('/api/passives', methods=['GET'])
def list_passives():
    message = {"type": "", "message": ""}
    try:
        user = request.args['user']
        passives = passive_model.list_passives(user)  # Se llama al modelo para listar usuarios
        return json.dumps(passives, default=str)
    except Exception as exception:
        print("======LIST_PASSIVES=====")
        print(exception)
        message["type"] = "error_interno"
        message["message"] = "Error en la conexion con la base de datos"
        return jsonify(message)

@passives_app.route('/api/passives', methods=['POST'])
def create_passive():
    passive = request.json['passive']
    print(passive)
    message = {"type": "", "message": ""}
    try:
        # Se llama al modelo para crear pasivos
        message = passive_model.save_passive(passive)
        return jsonify(message)
    except Exception as exception:
        print("======REG_NEW_PASSIVE=====")
        print(exception)
        message["type"] = "error_interno"
        message["message"] = "Error en la conexion con la base de datos"
        return jsonify(message)