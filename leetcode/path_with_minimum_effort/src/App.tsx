import React from 'react';
import { observable, IObservable } from 'mobx';
import { observer } from 'mobx-react';
import './App.css';

interface Node {
  height: number;
  status?: string;
  visited: boolean;
}

type Matrix = Node[][];

class Grid {
  @observable grid: Matrix;

  constructor(heights: number[][]) {
    const transformed_heights = heights.map(
      (row: number[]) => row.map(
        (h: number) => (
          { height: h, status: undefined, visited: false }
        )
      ));

    this.grid = observable(transformed_heights);

  }
}

// const heights = [[1,2,2],[3,8,2],[5,3,5]]
const heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]];
const gridInstance = new Grid(heights);
(window as any).gridInstance = gridInstance;


const Cell = observer(({ node }: { node: Node } ) =>
  <div className="cell">{node.height}</div>);

function Row({ row }: { row: Node[] }) {
  return <div className="row"> { row.map((n, i) => <Cell key={i} node={n} />) } </div>
}


function App() {
  return (
    <div className="App">
      <div className="grid">
        { gridInstance.grid.map((r, i) => <Row key={i} row={r} />) }
      </div>
    </div>
  );
}

function between(min: number, n: number, max: number) {
  // x in [min, max)
  return min <= n && n < max;
}

class BruteForce {
  rows: number;
  cols: number;
  upper_diff_limit: number = Infinity;
  heights: Node[][]

  constructor(heights: Node[][]) {
    this.rows = heights.length;
    this.cols = heights[0].length;
    this.heights = heights;
  }

  set_visited = (node: Node) => {
    node.height = 0
    node.visited = true;
  }

  minimumEffortPath = () => {
    const dfs = (x: number, y: number, max_difference: number) => {
      if (x === this.rows-1 && y === this.cols-1) {
        this.upper_diff_limit = Math.min(max_difference, this.upper_diff_limit);

        return max_difference;
      }

      const current_height =  this.heights[x][y].height;
      let min_effort = Infinity;

      this.set_visited(this.heights[x][y])


      for (let [dx, dy] of [[0, -1], [0, 1], [-1, 0], [1, 0]]) {
        const adj_x = x + dx;
        const adj_y = y + dy;
        const adj_height = this.heights[adj_x][adj_y].height;

        if (between(0, adj_x, this.rows) && between(0, adj_y, this.cols) && adj_height !== 0) {
          const current_diff = Math.abs(adj_height - current_height);
          // max difference ("effort") along the current path
          // if the current
          const max_current_diff = Math.max(max_difference, current_diff);

        }
      }



    }

    return dfs(0, 0, 0);
  }


}

const solution = new BruteForce(gridInstance.grid);

export default App;
