import React from "react";

import { GridNode } from '../stores';
import { Cell } from './Cell';

export function Row({ row }: { row: GridNode[] }) {
  return <div className="row"> { row.map((n, i) => <Cell key={i} node={n} />) } </div>
}