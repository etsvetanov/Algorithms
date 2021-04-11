import {observer} from "mobx-react";
import React, {useContext} from "react";
import classNames from "classnames";


import { Context } from '../App';
import {DIRECTIONS, GridNode} from '../stores';
import { BruteForce } from '../algorithms/bruteForce';

export const Cell = observer(({node}: { node: GridNode }) => {
  const finalClassname = classNames('cell', {
    visited: node.visited
  });

  const solution: BruteForce = useContext(Context);

  const transitionStripClasses = classNames('transition', 'transition--horizontal', {
    // 'transition--horizontal': node.transition_to === DIRECTIONS.LEFT || node.transition_to === DIRECTIONS.RIGHT,
    // 'transition--vertical': node.transition_to === DIRECTIONS.TOP || node.transition_to === DIRECTIONS.BOTTOM,
    'transition--left': node.transition_to === DIRECTIONS.LEFT,
    'transition--right': node.transition_to === DIRECTIONS.RIGHT,
    'transition--top': node.transition_to === DIRECTIONS.TOP,
    'transition--bottom': node.transition_to === DIRECTIONS.BOTTOM,
    'transition--bad': node.transition_bad === true
  });

  return (<div className={finalClassname}>
    {node.height}
    {node.transition_to && <div className={transitionStripClasses}> {`${node.transition_diff} (${solution.max_difference})`} </div>}
  </div>)
});
