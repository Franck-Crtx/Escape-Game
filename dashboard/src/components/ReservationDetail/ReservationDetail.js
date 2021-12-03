import React, { Component } from 'react';
import './Reservation.css';

function ReservationAcheteur(props) {
    var table = []

    let civilite = (props.acheteur.civilite == 0) ? 'Monsieur' : 'Madame';
    table.push(<li>{'Nom: ' + props.acheteur.nom} , </li>);
    table.push(<li>{'Prénom: ' + props.acheteur.prenom} , </li>);
    table.push(<li>{'Âge: ' + props.acheteur.age} , </li>);
    table.push(<li>{'Civilité: ' + civilite} , </li>);
    table.push(<li>{'Email: ' + props.acheteur.email}</li>);
    return table
}

function ReservationGame(props) {
    var table = []

    let vr = (props.game.vr == 0) ? 'Non' : 'Oui';
    let jours = props.game.jour.split(' ');
    var jour = '';
    for (let i = 0; i < 4; i++) {
        jour += jours[i];
        jour += ' ';
    }
    jour = jour.replace(',', '');
    table.push(<li>{'Nom: ' + props.game.nom} , </li>);
    table.push(<li>{'Jour: ' + jour} , </li>);
    table.push(<li>{'Horaire: ' + props.game.horaire} , </li>);
    table.push(<li>{'VR: ' + vr}</li>);    
    return table
}

function ReservationThemes(props) {
    var table = []

    for (let i = 0; i < props.themes.length; i++) {
        table.push(<li>{props.themes[i].type + ': ' + props.themes[i].nom}</li>)
    }
    return table
}

function ReservationSpectateurs(props) {
    var table = []

    for (let i = 0; i < props.spectateurs.length; i++) {
        let civilite = (props.spectateurs[i].civilite == 0) ? 'Monsieur' : 'Madame';
        let text = 'Nom: ' + props.spectateurs[i].nom;
        text += ', Prénom: ' + props.spectateurs[i].prenom;
        text += ', Age: ' + props.spectateurs[i].age;
        text += ', Civilité: ' + civilite;
        text += ', ' + props.spectateurs[i].tarif_nom;
        table.push(<li>{text}</li>)
    }
    return table
}

class ReservationDetail extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            acheteur: {
                nom: '',
                prenom: '',
                civilite: '',
                email: '',
                age: '',
            },
            game: {
                nom: '',
                horaire: '',
                jour: '',
                vr: ''
            },
            themes: [],
            spectateurs: [],
            isLoaded: false,
        }
    }


    componentDidMount() {
        fetch("http://127.0.0.1:5000/reservation?id=" + this.props.id)
        .then(res => res.json())
        .then((result) => {
            this.setState({
                isLoaded: true,
                reservationIndex: this.props.id,
                game: result.game,
                acheteur: result.acheteur,
                themes: result.themes,
                spectateurs: result.spectateurs
            });
        }, (error) => {
            this.setState({
                isLoaded: true,
                error
            });
        });
    }

    render() {
        const { error, reservationIndex, game, acheteur, themes, spectateurs} = this.state;
        if (error) {
            return <div>Erreur : {error.message}</div>;
        } else {
            return (
                <div className="modal">
                    <div className="header">Reservation No. {reservationIndex}</div>
                    <div className="separator"></div>
                    <div className="block_info">
                        <p className="title">Acheteur : </p>
                        <p className="info"><ReservationAcheteur acheteur={acheteur} /></p>
                    </div>
                    <div className="separator"></div>
                    <div className="block_info">
                        <p className="title">Game : </p>
                        <p className="info"><ReservationGame game={game} /></p>
                    </div>
                    <div className="separator"></div>
                    <div className="block_info">
                        <p className="title">Themes : </p>
                        <p className="info"><ReservationThemes themes={themes} /></p>
                    </div>
                    <div className="separator"></div>
                    <div className="block_info">
                        <p className="title">Spectateurs : </p>
                        <p className="info"><ReservationSpectateurs spectateurs={spectateurs} /></p>
                    </div>
                    <div className="separator"></div>
                </div>
            );
        }
    }
}

export default ReservationDetail;
