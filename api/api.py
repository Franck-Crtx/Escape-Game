import pymysql

from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from flask_cors import CORS
from flaskext.mysql import MySQL

import sys
import werkzeug, os

from subprocess import check_output, CalledProcessError, STDOUT
import time

from datetime import date

sys.path.insert(0, './routes')
from acheteur import *
from reservation import *
from theme import *
from login import *
from statistiques import *


CORS(app)

api = Api(app)

class Home(Resource):
    def get(self):
        return {'message':'Welcome Friends'}

api.add_resource(PostLogin, '/login')
api.add_resource(PostSubscribe, '/subscribe')
api.add_resource(PostAcheteur, '/acheteur')
api.add_resource(AllReservations, '/reservations')
api.add_resource(GetReservationById, '/reservation')
api.add_resource(AllThemes, '/themes')
api.add_resource(AllStatistiques, '/statistiques')

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
