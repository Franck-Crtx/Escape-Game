import pymysql
import datetime
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs

class AllStatistiques(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', type=int)
        parser.add_argument('offset', type=int)
        args = parser.parse_args()

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        result = {
            "homme": "50",
            "femme": "50",
            "age_one": "10",
            "age_two": "10",
            "age_three": "10",
            "age_four": "10",
            "age_five": "10",
            "not_vr" : "50",
            "vr": "50",
            "horaires": [],
            "games": []
        }

        sqlSexe = 'SELECT civilite, count(*) * 100.0 / sum(count(*)) over() as pourcent FROM spectateur GROUP BY civilite'
        sqlAge = 'SELECT SUM(CASE WHEN age < 18 THEN 1 ELSE 0 END) / COUNT(age) * 100 AS age_one, SUM(CASE WHEN age BETWEEN 18 AND 24 THEN 1 ELSE 0 END) / COUNT(age) * 100 AS age_two, SUM(CASE WHEN age BETWEEN 25 AND 39 THEN 1 ELSE 0 END) / COUNT(age) * 100 AS age_three, SUM(CASE WHEN age BETWEEN 40 AND 55 THEN 1 ELSE 0 END) / COUNT(age) * 100 AS age_four, SUM(CASE WHEN age > 55 THEN 1 ELSE 0 END) / COUNT(age) * 100 AS age_five FROM spectateur'
        sqlVR = 'SELECT reservation.vr, count(*) * 100.0 / sum(count(*)) over() as pourcent FROM spectateur INNER JOIN reservation_has_spectateurs ON reservation_has_spectateurs.spectateur_id = spectateur.id INNER JOIN reservation ON reservation_has_spectateurs.reservation_id = reservation.id GROUP BY reservation.vr'
        sqlHoraire = 'SELECT reservation.horaire, count(*) * 100.0 / sum(count(*)) over() as pourcent FROM spectateur INNER JOIN reservation_has_spectateurs ON reservation_has_spectateurs.spectateur_id = spectateur.id INNER JOIN reservation ON reservation_has_spectateurs.reservation_id = reservation.id GROUP BY reservation.horaire'
        sqlGame = 'SELECT game.nom, count(*) * 100.0 / sum(count(*)) over() as pourcent FROM spectateur INNER JOIN reservation_has_spectateurs ON reservation_has_spectateurs.spectateur_id = spectateur.id INNER JOIN reservation ON reservation_has_spectateurs.reservation_id = reservation.id INNER JOIN game on game.id = reservation.game_id GROUP BY game.nom'

        cursor.execute(sqlSexe)
        sexe = cursor.fetchall()

        cursor.execute(sqlAge)
        age = cursor.fetchone()

        cursor.execute(sqlVR)
        vr = cursor.fetchall()

        cursor.execute(sqlHoraire)
        horaires = cursor.fetchall()

        cursor.execute(sqlGame)
        games = cursor.fetchall()

        result['homme'] = str(sexe[0]['pourcent'])
        result['femme'] = str(sexe[1]['pourcent'])
        result['age_one'] = str(age['age_one'])
        result['age_two'] = str(age['age_two'])
        result['age_three'] = str(age['age_three'])
        result['age_four'] = str(age['age_four'])
        result['age_five'] = str(age['age_five'])
        result['not_vr'] = str(vr[0]['pourcent'])
        result['vr'] = str(vr[1]['pourcent'])

        for horaire in horaires:
            horaire['pourcent'] = str(horaire['pourcent'])    
            x = str(horaire['horaire']).split(':')
            horaire['horaire'] = x[0] + 'h' + x[1]
        result['horaires'] = horaires

        for game in games:
            game['pourcent'] = str(game['pourcent'])    
        result['games'] = games

        resp = jsonify(result)
        resp.status_code = 200
        return resp

