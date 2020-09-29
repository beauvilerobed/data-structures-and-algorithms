const clonedeep = require('lodash/clonedeep');

function doThirtyItrMincut(graph) {
  var graphKeys = Object.keys(graph);
  var numVertexes = graphKeys.length;
  var crossingEdges = 2 * numVertexes;

  var iterate = 30;
  var minimumCut = graph;

  while (iterate > 0) {
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
  var randomEdge = edges[Math.floor(Math.random() * edges.length)];
  var vertex = randomEdge[0];
  var vertexToMerge = randomEdge[1];
  var edgesOfGraphVertex = graph[vertex];

  var mergeVertexName = vertex;
  var edgesOfGraphMergeVertex = graph[vertexToMerge];

  penultimateEdges = edgesOfGraphVertex.concat(edgesOfGraphMergeVertex);
  finalEdges = [];

  for (v of penultimateEdges) {
      if ((v != vertex) && (v != vertexToMerge)) {
          finalEdges.push(v);
      }
  }

  delete graph[vertex];
  delete graph[vertexToMerge];

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

  return computeMincut(graph);
}

module.exports = doThirtyItrMincut;