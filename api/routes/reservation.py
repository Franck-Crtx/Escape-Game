import pymysql
import datetime
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs

class AllReservations(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', type=int)
        parser.add_argument('offset', type=int)
        args = parser.parse_args()

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlReservation = 'SELECT reservation.id, acheteur.nom, acheteur.prenom, game.nom AS nom_game, COUNT(reservation_has_spectateurs.spectateur_id) AS nb_spectateurs, theme.nom AS theme, reservation.jour, reservation.horaire, SUM(tarif.prix) AS montant_total FROM `reservation` INNER JOIN `login` ON login.id = reservation.login_id INNER JOIN `acheteur` ON acheteur.login_id = login.id INNER JOIN `reservation_has_spectateurs` ON reservation.id = reservation_has_spectateurs.reservation_id INNER JOIN `tarif` ON reservation_has_spectateurs.tarif_id = tarif.id INNER JOIN `game` ON reservation.game_id = game.id INNER JOIN `game_has_themes` ON reservation.game_id = game_has_themes.game_id AND game_has_themes.type_theme = 1 INNER JOIN `theme` ON theme.id = game_has_themes.theme_id GROUP BY reservation.id LIMIT {} OFFSET {}'.format(args['limit'], args['offset'])
        cursor.execute(sqlReservation)
        reservations = cursor.fetchall()

        sqlCount = 'SELECT count(id) AS nb_reservation FROM `reservation`'
        cursor.execute(sqlCount)
        count = cursor.fetchone()

        if not reservations:
            return jsonify({'about':'no reservations found'})
        for reservation in reservations:
            reservation['horaire'] = str(reservation['horaire'])

        resp = jsonify({"count": count['nb_reservation'], "reservations": reservations})
        resp.status_code = 200
        return resp

class GetReservationById(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()

        reservation = {
            'acheteur': {},
            'game': {},
            'themes': [],
            'spectateurs': []
        }

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlGame = 'SELECT game.nom, reservation.horaire, reservation.jour, reservation.vr FROM `reservation` INNER JOIN `game` ON game.id = reservation.game_id AND reservation.id = {}'.format(args['id'])
        sqlAcheteur = 'SELECT acheteur.nom, acheteur.prenom, acheteur.age, acheteur.civilite, acheteur.email FROM `reservation` INNER JOIN `login` ON login.id = reservation.login_id INNER JOIN `acheteur` ON acheteur.login_id = login.id AND reservation.id = {}'.format(args['id'])
        sqlSpectateurs = 'SELECT spectateur.nom, spectateur.prenom, spectateur.civilite, spectateur.age, tarif.nom AS tarif_nom FROM `reservation` INNER JOIN `reservation_has_spectateurs` ON reservation_has_spectateurs.reservation_id = reservation.id INNER JOIN `spectateur` ON spectateur.id = reservation_has_spectateurs.spectateur_id INNER JOIN tarif ON tarif.id = reservation_has_spectateurs.tarif_id AND reservation.id = {}'.format(args['id'])
        sqlThemes = 'SELECT type_theme.nom AS type, theme.nom AS nom FROM `reservation` INNER JOIN `game` ON game.id = reservation.game_id INNER JOIN `game_has_themes` ON game_has_themes.game_id = game.id INNER JOIN `theme` ON theme.id = game_has_themes.theme_id INNER JOIN `type_theme` ON type_theme.id = game_has_themes.type_theme AND reservation.id = {}'.format(args['id'])

        cursor.execute(sqlGame)
        game = cursor.fetchone()

        cursor.execute(sqlAcheteur)
        acheteur = cursor.fetchone()
 
        cursor.execute(sqlSpectateurs)
        spectateurs = cursor.fetchall()
 
        cursor.execute(sqlThemes)
        themes = cursor.fetchall()

        game['horaire'] = str(game['horaire'])
        reservation['game'] = game
        reservation['acheteur'] = acheteur
        reservation['themes'] = themes
        reservation['spectateurs'] = spectateurs
        resp = jsonify(reservation)
        resp.status_code = 200
        return resp

