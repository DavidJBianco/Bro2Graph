// Shortest path between two vertices
def shortest_path(v1, v2, hops) {

  p = g.v(v1).as("x").outE.inV.loop("x"){it.loops < hops}{it.object == g.v(v2)}.path.next()
  
  p
}
