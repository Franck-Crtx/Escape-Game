import React from 'react';
import { Link } from 'react-router-dom';

export default function Statistiques() {
    return(
        <div>
            <h2>Home</h2>
                <ul>
                    <li><Link to="/reservations">Réservations</Link></li>
                    <li><Link to="/statistiques">Statistiques</Link></li>
                </ul>
        </div>
    );
}