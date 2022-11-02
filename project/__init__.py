# -*- coding: utf-8 -*-
from flask import Flask, current_app, g, render_template
from flask_pymongo import PyMongo, pymongo
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()


# Instancia de la aplicación de flask
app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, resources= { r"/*": {"origins": "*"} })

# Configuración de la base de datos Mongo y su conección
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

client = pymongo.MongoClient(os.getenv('MONGO_URI'))
db = client.get_database('Lignum')

# Definición de rutas de Blueprint
from project.api.passives import passives_app

#Instancias del blueprint
app.register_blueprint(passives_app)

@app.route('/api')
def index():
    return 'Server on'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def angular(path):
    return render_template('index.html')