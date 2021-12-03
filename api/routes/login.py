import pymysql
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

class PostSubscribe(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('result', type=dict, location='json')
        args = parser.parse_args()['result']
        
        print("password: " + args['password'])
        key = load_key()
        password = args['password'].encode()
        f = Fernet(key)
        password = f.encrypt(password)
        print("password: " + str(password))

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        sqlLogin = 'INSERT INTO `login` (`state`) VALUES (1)'
        cursor.execute(sqlLogin)
        login_id = conn.insert_id()

        sqlSubscribe = 'INSERT INTO `user` (`login_id`, `nom`, `prenom` , `email`, `password`) VALUES ({}, "{}", "{}", "{}", "{}")'.format(login_id, args['nom'], args['prenom'], args['email'], str(password))
        cursor.execute(sqlSubscribe)
        conn.commit()
        return "created"

class PostLogin(Resource):
    def post(self):
        result = {'token': ''}
        parser = reqparse.RequestParser()
        parser.add_argument('result', type=dict, location='json')
        args = parser.parse_args()['result']

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sqlLogin = 'SELECT password FROM `user` WHERE email = "{}"'.format(args['email'])
        cursor.execute(sqlLogin)

        row = cursor.fetchone()

        if row is None:
            return jsonify(result)
        password_sql = row['password']
        password_sql = password_sql.replace("b'", "")
        password_sql = password_sql.replace("'", "")
        password_sql = password_sql.encode()
        key = load_key()
        f = Fernet(key)
        password_sql = f.decrypt(password_sql)
        password_sql = password_sql.decode()

        if args['password'] == password_sql:
            result = {'token': 'J3Byb8cEaGpDPGpPb55x5Sh'}
        return jsonify(result)        
