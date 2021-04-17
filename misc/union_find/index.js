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

const uf = new UnionFind(10);




const getNodesFromArr = arr => {
  const data = arr.map(x => ({id: x, label: `Node ${x}`}));

  return new vis.DataSet(data);
}


const union_set = getInitialArr(10);

var nodes = getNodesFromArr(union_set);


// var nodes = new vis.DataSet([
//   {id: 1, label: "Node 1"},
//   {id: 2, label: "Node 2"},
//   {id: 3, label: "Node 3"},
//   {id: 4, label: "Node 4"},
//   {id: 5, label: "Node 5", color: "#f1ad69"},
// ]);

window.nodes = nodes;

// create an array with edges
// var edges = new vis.DataSet([
//   {from: 1, to: 3},
//   {from: 1, to: 2},
//   {from: 2, to: 4},
//   {from: 2, to: 5},
//   {from: 3, to: 3},
// ]);

var edges = new vis.DataSet();

window.edges = edges;

// create a network
var container = document.getElementById("mynetwork");
var data = {
  nodes: nodes,
  edges: edges,
};
window.data = data;
var options = {};
var network = new vis.Network(container, data, options);
window.netork = network;
