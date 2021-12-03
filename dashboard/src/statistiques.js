import React, { Component } from 'react';
import CanvasJSReact from "./lib/canvasjs.react";

var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class Statistiques extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            statistiques: {
                homme: '',
                femme: '',
                age_one: '',
                age_two: '',
                age_three: '',
                age_four: '',
                age_five: '',
                not_vr: '',
                vr: '',
                horaires: [],
                games: []
            },
            isLoaded: false
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:5000/statistiques")
            .then(res => res.json())
            .then((result) => {
                this.setState({
                    statistiques: {
                        homme: result.homme,
                        femme: result.femme,
                        age_one: result.age_one,
                        age_two: result.age_two,
                        age_three: result.age_three,
                        age_four: result.age_four,
                        age_five: result.age_five,
                        not_vr: result.not_vr,
                        vr: result.vr,
                        horaires: result.horaires,
                        games: result.games
                    },
                    isLoaded: true
                });
            }, (error) => {
                this.setState({
                    isLoaded: true,
                    error
                });
            });
    }

    render() {
        const { error, statistiques } = this.state;
        if (error) {
            return <div>Erreur : {error.message}</div>;
        }

        let dataPointsHoraires = [];
        for (let i = 0; i < statistiques.horaires.length; i++) {
           dataPointsHoraires[i] = {y: statistiques.horaires[i].pourcent, label: statistiques.horaires[i].horaire}
        }
        
        let dataPointsGames = [];
        for (let i = 0; i < statistiques.games.length; i++) {
           dataPointsGames[i] = {y: statistiques.games[i].pourcent, label: statistiques.games[i].nom}
        }

        const options_sexe = {
			animationEnabled: true,
			exportEnabled: true,
			theme: "dark2",
			title:{
				text: "Repartion par sexe"
			},
			data: [{
				type: "pie",
				indexLabel: "{label}: {y}%",		
				startAngle: -90,
				dataPoints: [
					{ y: statistiques.homme, label: "Homme" },
					{ y: statistiques.femme, label: "Femme" },
				]
			}]
		}
        const options_age = {
			animationEnabled: true,
			exportEnabled: true,
			theme: "dark1",
			title:{
				text: "Repartion par âge"
			},
			data: [{
				type: "pie",
				indexLabel: "{label}: {y}%",		
				startAngle: -90,
				dataPoints: [
					{ y: statistiques.age_one, label: "< 18 ans" },
					{ y: statistiques.age_two, label: "18-25 ans" },
                    { y: statistiques.age_three, label: "25-39 ans" },
                    { y: statistiques.age_four, label: "40-54 ans" },
                    { y: statistiques.age_five, label: "> 55 ans" }

				]
			}]
		}
        const options_vr = {
			animationEnabled: true,
			exportEnabled: true,
			theme: "dark2",
			title:{
				text: "Repartion par VR"
			},
			data: [{
				type: "pie",
				indexLabel: "{label}: {y}%",		
				startAngle: -90,
				dataPoints: [
					{ y: statistiques.not_vr, label: "Sans VR" },
					{ y: statistiques.vr, label: "VR" },
				]
			}]
		}
        const options_horaires = {
			animationEnabled: true,
			exportEnabled: true,
			theme: "dark1",
			title:{
				text: "Repartion par horaires"
			},
			data: [{
				type: "pie",
				indexLabel: "{label}: {y}%",		
				startAngle: -90,
				dataPoints: dataPointsHoraires
			}]
		}
        const options_games = {
			animationEnabled: true,
			exportEnabled: true,
			theme: "dark2",
			title:{
				text: "Repartion par jeux"
			},
			data: [{
				type: "pie",
				indexLabel: "{label}: {y}%",		
				startAngle: -90,
				dataPoints: dataPointsGames
			}]
		}
        return (
            <div>
                <h2>Statistiques</h2>
                <CanvasJSChart options = {options_sexe} />
                <CanvasJSChart options = {options_age} />
                <CanvasJSChart options = {options_vr} />
                <CanvasJSChart options = {options_horaires} />
                <CanvasJSChart options = {options_games} />
		    </div>
        );
    }
}

export default Statistiques;
