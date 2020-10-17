var timePass = 0;
var leader = null;

class Node {
  constructor(_id, edges) {
    this.id = _id;
    if (edges === null) {
        this.edges = {};
    } else {
        this.edges = edges;
    }
    this.edges = {};
    this.explored = false;
    this.finished = false;
  }
}

class Graph {
  constructor() {
      this.nodes = {};
  }

  addNode(node) {
      this.nodes.push(node);
      this.edges[nodes] = [];
  }

  addDirectedEdge(node1, node2) {
      this.edges[node1].push(node2);
  }
}

function kosarajuTwoPass(graph) {
  graphRev = reverseGraph(graph);
  dfsLoop(graphRev);
  dfsLoop(graph)
}

function dfsLoop(graph) {
  for (var j = graphLength - 1; j >= 0; i--) {
      if (graph[j][2] === null) {
          leader = graph[j];
      }
  }
}

function dfs(graph, node){
  for (var k = 0; k < graph.length; k++) {
    if (graph[k][2] === null) {
      dfs(graph, k)
    }
  }
  timePass = timePass + 1
  graph[node].push(timePass)
}