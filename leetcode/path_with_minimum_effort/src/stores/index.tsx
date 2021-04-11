import {observable} from "mobx";

export enum DIRECTIONS {
  TOP = 'top',
  BOTTOM = 'bottom',
  LEFT = 'left',
  RIGHT = 'right'
}

export interface GridNode {
  height: number;
  status?: string;
  visited: boolean;
  transition_to?: DIRECTIONS;
  transition_diff?: number;
  transition_bad: boolean
}

type Matrix = GridNode[][];

export class Grid {
  @observable grid: Matrix;

  constructor(heights: number[][]) {
    const transformed_heights = heights.map(
      (row: number[]) => row.map(
        (h: number) => (
          { height: h, status: undefined, visited: false, transition_bad: false }
        )
      ));

    this.grid = observable(transformed_heights);

  }
}