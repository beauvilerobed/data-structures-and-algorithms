const clonedeep = require('lobash.clonedeep');

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

  for (k in graph) {
    for (e in graph[k]) {
      var edge = [k, e];
      edges.push(edge);
    }
  }
  
  var randomEdge = edge[Math.floor(Math.random() * edges.length)];
  var vertex = randomEdge[0];
  var vertexToMerge = randomEdge[1];
  var edgesOfGraphVertex = graph[vertex];

  var mergeVertexName = vertex;
  var edgesOfGraphMergeVertex = graph[vertexToMerge];
  
  
  penultimateEdges = edgesOfGraphVertex + edgesOfGraphMergeVertex;
  finalEdges = penultimateEdges.filter(v => (v !== vertex) && (v !== vertexToMerge));

  delete graph.vertex;
  delete graph.vertexToMerge;

  for (k in graph) {
    tempEdges = [];
    for (edge in graph[k]) {
      if ((edge === vertex) || (edge === vertexToMerge)) {
        tempEdges.push(mergeVertexName);
      } else {
        tempEdges.push(edge);
      }
    }
    graph[k] = tempEdges;
  }
  graph[vertexToMerge] = finalEdges;
  return computeMincut(graph);
}

module.exports = doThirtyItrMincut;