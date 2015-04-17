// Return info about the count of different types of vertices and edges
def graph_info() {

  numv = g.V.count()
  nume = g.E.count()
  vinfo = g.V.groupBy{it.element_type}{1}{it.size}.cap.next()
  einfo = g.E.groupBy{it.element_type}{1}{it.size}.cap.next()

  return [numv: numv, nume: nume, vinfo: vinfo, einfo: einfo]
}

// Shortest path between two vertices
def shortest_path(v1, v2, hops) {

  p = g.v(v1).as("x").outE.inV.loop("x"){it.loops < hops}{it.object == g.v(v2)}.path.next()
  
  p
}
