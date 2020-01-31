import React from 'react';
import './App.css';
import {BrowserRouter, Route, Link} from 'react-router-dom'
// Rotas
import CadastroCurriculo from './rotas/cadastro-curriculo'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Route exact={true} path='/trabalhe_conosco' component={CadastroCurriculo} />
        <Route exact={true} path='/' component={CadastroCurriculo} />
      </BrowserRouter>
    </div>
  );
}

export default App;
