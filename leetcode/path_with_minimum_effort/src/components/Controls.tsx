import React, {useContext} from "react";
import {observer} from 'mobx-react';

import {BruteForce} from "../algorithms/bruteForce";
import {Context} from "../App";


export const Controls = observer(() => {
  const solution: BruteForce = useContext(Context);

  return (<div className="controls">
    <button onClick={solution.handleNext} className="btn btn-next">Next</button>

    <div className="controls__info">
      <span> answer: </span>
      <span> {solution.answer !== undefined ? solution.answer : 'n/a'} </span>
      <span> upper_diff_limit: </span>
      <span> {solution.upper_diff_limit} </span>
    </div>

  </div>)
});
