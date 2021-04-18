// create an array with nodes

const getInitialArr = n => {
  const arr = [];

  for (let i=0;i<10; i++) {
    arr[i] = i;
  }

  return arr;
}

function intersection(setA, setB) {
  let _intersection = new Set()
  for (let elem of setB) {
    if (setA.has(elem)) {
      _intersection.add(elem)
    }
  }
  return _intersection
}

class UnionFind {
  constructor(n) {
    this._arr = getInitialArr(n);
  }

  union(a, b) {
    /**
      Connect a and b
    */
    const leader = this._arr[a];

    for (let i=0; i<this._arr.length; i++) {
      if (this._arr[i] === b) {
        this._arr[i] = leader;
      }
    } 
  }

  find(a, b) {
    /**
      Find if a and b belong to the same connected component
    */

    return this._arr[a] === this._arr[b];
  }
}

class UnionControl {
  constructor(uf, network ) {
    this.uf = uf;
    this.network = network;


    this.redraw();
  }

  getNodesSet() {
    const nodes = this.uf._arr.map((x, i) => ({ id: i, label: `Node ${i}`}));

    return new vis.DataSet(nodes);
  }

  getEdgesSet() {
    const edges = this.uf._arr.map((x, i) => ({ from: i, to: x }));

    return new vis.DataSet(edges);
  }

  redraw() {
    const data = {
      nodes: this.getNodesSet(),
      edges: this.getEdgesSet()
    }

    window.data = data;

    this.network.setData(data);
  }

  union(a, b) {
    this.uf.union(a, b);

    this.redraw();
  }

  find(a, b) {
    return this.uf.find(a, b);
  }
}

const uf = new UnionFind(10);


var container = document.getElementById("mynetwork");

var options = {};
var data = {};

var network = new vis.Network(container, data, options);
var ctrl = new UnionControl(uf, network);


window.ctrl = ctrl;
window.netork = network;
