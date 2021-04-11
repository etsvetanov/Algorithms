import React from 'react';

import {Row} from './components/Row';
import {Controls} from './components/Controls';
import {Grid, GridNode} from './stores';
import { BruteForce } from './algorithms/bruteForce'
import './App.css';

import { isObservable, isObservableProp } from 'mobx';


(window as any).isObservableProp = isObservableProp;

// const heights = [[1,2,2],[3,8,2],[5,3,5]]
const heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]];
const gridInstance = new Grid(heights);
(window as any).gridInstance = gridInstance;
const solution = new BruteForce(gridInstance);
(window as any).solution = solution;


export const Context = React.createContext(solution);

function App() {
  return (
    <div className="App">
      <Context.Provider value={solution}>
        <div className="grid">
          {gridInstance.grid.map((r, i) => <Row key={i} row={r}/>)}
        </div>


        <Controls />
      </Context.Provider>

    </div>
  );
}



export default App;
