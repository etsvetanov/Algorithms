import {observable, makeObservable} from "mobx";

import {Grid, GridNode, DIRECTIONS} from "../stores";
import {between} from '../utils'

const DIRECTION_BY_COORDINATES: {[index: string]: string} = {
  '0,1': DIRECTIONS.RIGHT,
  '0,-1': DIRECTIONS.LEFT,
  '-1,0': DIRECTIONS.TOP,
  '1,0': DIRECTIONS.BOTTOM
}


export class BruteForce {
  rows: number;
  cols: number;
  upper_diff_limit: number = Infinity;
  heights: GridNode[][];
  it: Iterator<any>;
  answer?: number;
  max_difference: number = 0;

  _on_next: (() => void)[] = [];

  onNext = (fn: () => void) => {
    this._on_next.push(fn);
  }

  exec_on_next = () => {
    for (const fn of this._on_next) {
      fn();
    }
  }


  constructor(gridInstance: Grid) {
    const heights = gridInstance.grid;
    this.rows = heights.length;
    this.cols = heights[0].length;
    this.heights = heights;
    this.it = this.dfs(0, 0, 0);

    makeObservable(this, {
      upper_diff_limit: observable,
      answer: observable,
      max_difference: observable
    })
  }

  set_visited = (node: GridNode) => {
    node.height = 0
    node.visited = true;
  }

  handleNext = () => {
    this.exec_on_next();


    const res = this.it.next();

    if (res.done) {
      this.answer = res.value;
    }

    return res.done
  }

  revert_height = (x: number, y: number, height: number) => {
      this.heights[x][y].height = height;
      this.heights[x][y].visited = false;

  }

  // dispose_transition?: () => void;

  set_transition = (x: number, y: number, dx: number, dy: number, transition_diff: number) => {


    const node = this.heights[x][y];

    node.transition_to = DIRECTION_BY_COORDINATES[[dx, dy].toString()] as DIRECTIONS
    node.transition_diff = transition_diff;

    this.onNext(() => { node.transition_to = undefined });
  }

  set_bad_path = (x: number, y: number, dx: number, dy: number, transition_diff: number) => {
    const node = this.heights[x][y];
    node.transition_bad = true;
    node.transition_to = DIRECTION_BY_COORDINATES[[dx, dy].toString()] as DIRECTIONS
    node.transition_diff = transition_diff;
    this.onNext(() => { node.transition_to = undefined; node.transition_bad = false})
  }



  * dfs(x: number, y: number, max_difference: number): any {
    this.max_difference = max_difference;

    if (x === this.rows - 1 && y === this.cols - 1) {
      this.upper_diff_limit = Math.min(max_difference, this.upper_diff_limit);

      return max_difference;
    }

    const current_height = this.heights[x][y].height;
    let min_effort = Infinity;

    // yield;

    this.set_visited(this.heights[x][y])



    for (let [dx, dy] of [[0, -1], [0, 1], [-1, 0], [1, 0]]) {
      const adj_x = x + dx;
      const adj_y = y + dy;


      if (between(0, adj_x, this.rows) && between(0, adj_y, this.cols) && this.heights[adj_x][adj_y].height !== 0) {

        const current_diff = Math.abs(this.heights[adj_x][adj_y].height - current_height);
        this.set_transition(x, y, dx, dy, current_diff);
        yield;

        /** max difference ("effort") along the current path
            if the current_max is more the max_difference, then update
         */
        const max_current_diff = Math.max(max_difference, current_diff);


        if (max_current_diff < this.upper_diff_limit) {
          const result = yield* this.dfs(adj_x, adj_y, max_current_diff);

          min_effort = Math.min(min_effort, result);
        } else {
          this.set_bad_path(x, y, dx, dy, current_diff);
          yield;
        }
      }
    }

    this.revert_height(x, y, current_height)

    return min_effort;
  }

  // minimumEffortPath = () => {
  //   return this.dfs(0, 0, 0)
  //
  //
  //   // return dfs(0, 0, 0);
  // }
}
