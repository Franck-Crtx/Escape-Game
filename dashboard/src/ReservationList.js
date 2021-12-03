import React, { Component } from 'react';
import MaterialTable from 'material-table';

import ReservationDetail from './components/ReservationDetail/ReservationDetail.js'

class ReservationList extends Component
{
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            theme_list: {}
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:5000/themes")
        .then(res => res.json())
        .then(
            (result) => {
                var tmp_themes={};
                for (let i = 0; i < result.length; i++)
                    tmp_themes[result[i].nom] = result[i].nom;
                this.setState({
                    theme_list: tmp_themes
                });
            },
            (error) => {
                this.setState({
                    error
                });
            }
        )
    }

    static filters(reservations, query)
    {
        reservations = reservations.filter(poke => poke.nom.includes(query.search));
        for (let i = 0; i < query.filters.length; i++) {
            if (query.filters[i].column.field === "theme")
                for (let j = 0; j < query.filters[i].value.length; j++)
                    reservations = reservations.filter(poke => poke.theme.includes(query.filters[i].value[j]));
            if (query.filters[i].column.field === "id")
                reservations = reservations.filter(poke => poke.id == query.filters[i].value);
            if (query.filters[i].column.field === "nom")
                reservations = reservations.filter(poke => poke.nom.startsWith(query.filters[i].value));
            if (query.filters[i].column.field === "prenom")
                reservations = reservations.filter(poke => poke.prenom.startsWith(query.filters[i].value));
            if (query.filters[i].column.field === "nom_game")
                reservations = reservations.filter(poke => poke.nom_game.includes(query.filters[i].value));
        }
        return reservations;
    }

    static displayJour(rowData) {
        var table = [];
        var jours = rowData.jour.split(' ');
        var jour = '';

        for (let i = 0; i < 4; i++) {
            jour += jours[i];
            jour += ' ';
        }
        table.push(<tr>{jour}</tr>);
        return table;
    }

    static displayMontant(rowData) {
        var table = [];
        var montant = rowData.montant_total
        table.push(<tr>{montant + ' €'}</tr>);
        return table;
    }

    render()
    {
        const { error, theme_list} = this.state;
        if (error) {
            return <div>Erreur : {error.message}</div>;
        } else {
            return (
                <MaterialTable
                    title="Reservations"
                    columns={[
                        { title: 'ID', field: 'id'},
                        { title: 'Nom', field: 'nom', type: 'string'},
                        { title: 'Prénom', field: 'prenom', type: 'string'},
                        { title: 'Game', field: 'nom_game', type: 'string'},
                        { title: 'Main Theme', field: 'theme', lookup: theme_list},
                        { title: 'Nombre spectateurs', field: 'nb_spectateurs', filtering: false},
                        { title: 'Jour', field: 'jour', render: (rowData) => ReservationList.displayJour(rowData), filtering: false},
                        { title: 'Horaire', field: 'horaire', type: 'string', filtering: false},
                        { title: 'Montant Total', field: 'montant_total', filtering: false, render: (rowData) => ReservationList.displayMontant(rowData)}
                    ]}
                    data={query =>
                        new Promise((resolve, reject) => {
                            let url = 'http://127.0.0.1:5000/reservations?'
                            url += 'offset=' + (query.page * query.pageSize)
                            url += '&limit=' + query.pageSize
                            fetch(url)
                            .then(response => response.json())
                            .then(result => {
                                result.reservations = ReservationList.filters(result.reservations, query)
                                resolve({
                                    data: result.reservations,
                                    page: query.page,
                                    totalCount: result.count
                                 })
                            })
                        })
                    }
                    options={{
                        search: false,
                        filtering: true,
                        pageSizeOptions: [5, 10, 20, 50],
                        headerStyle: {
                          backgroundColor: '#01579b',
                          color: '#FFF'
                        },
                        rowStyle: rowData => ({
                            backgroundColor: (rowData.tableData.id % 2 === 0) ? '#DDD' : '#FFF'
                        })
                    }}
                    detailPanel={[{
                        tooltip: 'Show Details',
                        render: rowData => {
                            return (
                                <ReservationDetail id={rowData.id} />
                            )
                        },
                    }]}
                    onRowClick={(event, rowData, togglePanel) => togglePanel()}
                />
            );
        }
    }
}

export default ReservationList;
