const clonedeep = require('lodash/clonedeep');

function doThirtyItrMincut(graph) {
  var graphKeys = Object.keys(graph);
  var numVertexes = graphKeys.length;
  var crossingEdges = 2 * numVertexes;

  var iterate = 30;
  let minimumCut = graph;

  while (iterate > 0) {
    console.log("iteration" + iterate)
    var newGraph = clonedeep(graph);
    var localMinimum = computeMincut(newGraph);
    var keys = Object.keys(localMinimum);
    var localMinCrossingEdges = localMinimum[keys[0]].length
    if (crossingEdges > localMinCrossingEdges) {
      crossingEdges = localMinCrossingEdges;
      minimumCut = localMinimum;
    }
    iterate = iterate - 1;
  }

  return crossingEdges;
}

function computeMincut(graph) {
  var graphLength = Object.keys(graph).length;
  if (graphLength <= 2) {
    return graph;
  }

  var edges = [];

  for (const k in graph) {
    for (const e of graph[k]) {
      var edge = [k, e];
      edges.push(edge);
    }
  }
  console.log(edges)
  var randomEdge = edges[Math.floor(Math.random() * edges.length)];
  console.log(randomEdge)
  var vertex = randomEdge[0];
  var vertexToMerge = randomEdge[1];
  console.log(vertexToMerge)
  var edgesOfGraphVertex = graph[vertex];

  var mergeVertexName = vertex;
  var edgesOfGraphMergeVertex = graph[vertexToMerge];
  console.log(edgesOfGraphVertex)
  console.log(edgesOfGraphMergeVertex)

  penultimateEdges = edgesOfGraphVertex.concat(edgesOfGraphMergeVertex);
  finalEdges = [];

  for (v of penultimateEdges) {
      if ((v != vertex) && (v != vertexToMerge)) {
          finalEdges.push(v);
      }
  }
  console.log(graph)
  delete graph[vertex];
  delete graph[vertexToMerge];
  console.log(graph)
  for (k in graph) {
    tempEdges = [];
    for (edge of graph[k]) {
      if ((edge == vertex) || (edge == vertexToMerge)) {
        tempEdges.push(parseInt(mergeVertexName));
      } else {
        tempEdges.push(edge);
      }
    }
    graph[k] = tempEdges;
  }
  graph[mergeVertexName] = finalEdges;
  console.log(graph)
  console.log("neeeeeext")
  return computeMincut(graph);
}

module.exports = doThirtyItrMincut;