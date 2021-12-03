import React, { useState } from 'react';
import Login from './login.js';
import Home from './home.js'
import ReservationList from './ReservationList.js'
import Statistiques from './statistiques.js'
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';
import useToken from './useToken.js';

function App() {
  const { token, setToken } = useToken();

  if (!token) {
    return <Login setToken={setToken} />
  }

  return (
    <div className="wrapper">
      <h1>VDM Escape Game</h1>
      <BrowserRouter>
        <Switch>
          <Route path="/reservations">
            <div className="App">
              <ReservationList />
            </div>
          </Route>
          <Route path="/statistiques">
            <Statistiques />
          </Route>
          <Route path="/">
            <div className="App">
              <Home />
            </div>
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );    
}

export default App;
