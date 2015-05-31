// Return info about the count of different types of vertices and edges
def graph_info() {

  numv = g.V.count()
  nume = g.E.count()
  vinfo = g.V.groupBy{it.element_type}{1}{it.size}.cap.next()
  einfo = g.E.groupBy{it.element_type}{1}{it.size}.cap.next()

  return [numv: numv, nume: nume, vinfo: vinfo, einfo: einfo]
}

// Shortest path between two vertices
def shortest_path(node1_id, node2_id, hops, directed) {

  if (directed) {
    p = g.v(node1_id).as("x").outE.inV.dedup.loop("x"){it.loops < hops}{it.object.id == node2_id.toString()}.path.sort{a,b -> a.size() <=> b.size()}.take(1)
  } else {
    p = g.v(node1_id).as("x").bothE.bothV.dedup.loop("x"){it.loops < hops}{it.object.id == node2_id.toString()}.path.sort{a,b -> a.size() <=> b.size()}.take(1)
  }
}

// Shortest path between two vertices, where the destination is a node
// type, not a specific node ID
def shortest_path_to_type(node1_id, node2_type, hops, directed) {

  if (directed) {
    p = g.v(node1_id).as("x").outE.inV.dedup.loop("x"){it.loops < hops}{it.object.element_type == node2_type}.path.sort{a,b -> a.size() <=> b.size()}.take(1)
  } else {
    p = g.v(node1_id).as("x").bothE.bothV.dedup.loop("x"){it.loops < hops}{it.object.element_type == node2_type}.path.sort{a,b -> a.size() <=> b.size()}.take(1)
  }
}

// Test script to get simple node info
def node_info(node_id) {
  n = g.v(node_id).map
  n
}

