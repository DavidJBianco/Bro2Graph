// Return info about the count of different types of vertices and edges
def graph_info() {

  numv = g.V.count()
  nume = g.E.count()
  vinfo = g.V.groupBy{it.element_type}{1}{it.size}.cap.next()
  einfo = g.E.groupBy{it.element_type}{1}{it.size}.cap.next()

  return [numv: numv, nume: nume, vinfo: vinfo, einfo: einfo]
}

// Shortest path between two vertices
def shortest_path(node1_id, node2_id, hops) {

  g.v(node1_id).as("x").outE.inV.loop("x"){it.loops < hops}{it.object == g.v(node2_id)}.path.sort{a,b -> a.count() <=> b.count()}.take(1)
}

// Test script to get simple node info
def node_info(node_id) {
  n = g.v(node_id).map
  n
}

