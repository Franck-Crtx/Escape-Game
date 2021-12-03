import pymysql
import datetime
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs

class AllThemes(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT theme.nom FROM `theme`')
        themes = cursor.fetchall()

        if not themes:
            return jsonify({'about':'no themes found'})
        resp = jsonify(themes)
        resp.status_code = 200
        return resp