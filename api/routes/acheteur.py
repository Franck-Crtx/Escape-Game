import pymysql
from app import app
from db_config import mysql
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, inputs

class PostAcheteur(Resource):
    game_index = {
        'Impot sur le revenu': 1,
        'Greve de la SNCF': 2,
        'Interminable attente chez le medecin': 3,
        'Soutenance finale': 4,
        'Mon compte en banque en fin du mois': 5,
        'Mariage sans alcool': 6,
        'Diner de famille insoutenable': 7,
        'Plus de PQ dans les toilettes': 8,
        'En plein dans la Friendzone': 9,
    }

    tarif_index = {
        'Plein tarif': 1,
        'Tarif reduit': 2,
        'Senior': 3,
        'Tarif etudiant': 4
    }

    def postAcheteur(self, conn, cursor, acheteur):
        civilite = 0 if acheteur['Civilite'] == 'Monsieur' else 1
        sqlLogin = 'INSERT INTO `login` (`state`) VALUES (1)'
        cursor.execute(sqlLogin)
        login_id = conn.insert_id()
        sqlAcheteur = 'INSERT INTO `acheteur`(`login_id`, `civilite`, `prenom`, `nom`, `age`, `email`) VALUES ({},{},"{}","{}",{},"{}")'.format(login_id, civilite, acheteur['Prenom'], acheteur['Nom'], acheteur['Age'], acheteur['Email'])
        cursor.execute(sqlAcheteur)
        return login_id

    def postReservation(self, conn, cursor, game, login_id):
        vr = 0 if game['VR'] == 'Non' else 1
        game_name = game['Nom']
        game_id = self.game_index[game_name]
        sqlReservation = 'INSERT INTO `reservation` (`login_id`, `game_id` , `jour`, `horaire`, `vr`) VALUES ({}, {}, "{}", "{}", {})'.format(login_id, game_id, game['Jour'], game['Horaire'], vr)
        cursor.execute(sqlReservation)
        return conn.insert_id()

    def postSpectateur(self, conn, cursor, reservations, reservation_id):
        for reservation in reservations:
            spectateur = reservation['Spectateur']
            civilite = 0 if spectateur['Civilite'] == 'Monsieur' else 1
            tarif = reservation['Tarif']
            tarif_id = self.tarif_index[tarif]
            sqlSpectateur = 'INSERT INTO `spectateur` (`civilite`, `nom` , `prenom`, `age`) VALUES ({}, "{}", "{}", {})'.format(civilite, spectateur['Nom'], spectateur['Prenom'], spectateur['Age'])
            cursor.execute(sqlSpectateur)
            spectateur_id = conn.insert_id()
            sqlReservationHasSpectateurs = 'INSERT INTO `reservation_has_spectateurs` (`reservation_id`, `tarif_id` , `spectateur_id`) VALUES ({}, {}, {})'.format(reservation_id, tarif_id, spectateur_id)
            cursor.execute(sqlReservationHasSpectateurs)
        return

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('result', type=dict, location='json')
        args = parser.parse_args()
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        login_id = self.postAcheteur(conn, cursor, args['result']['Acheteur'])
        reservation_id = self.postReservation(conn, cursor, args['result']['Game'], login_id)
        self.postSpectateur(conn, cursor, args['result']['Reservation'], reservation_id)
        conn.commit()
        return "Created"
