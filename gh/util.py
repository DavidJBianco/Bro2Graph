#!/usr/bin/env python

def _v2s(v):
    if not "_type" in v:
        return "-"
    elif v["_type"] == "vertex":
        return "v[id:%s %s %s]" % (v["_id"], v["element_type"], v["name"])
    elif v["_type"] == "edge":
        return "  e[id:%s inV:%s rel:%s outV:%s ]" % (v["_id"], v["_inV"], v["element_type"], v["_outV"])
    else:
        return "??"

def write_graphml(g, filename="/tmp/graph.graphml"):
    '''
    Given a Graph object (g), write the GraphML representation to the 
    given filename.  If no filename is given, use the default 
    "/tmp/graph.graphml".  This can be loaded into Gephi or some other
    visualization tool.
    '''
    gml = g.get_graphml()
    f = open(filename,"w")
    f.write(gml)
    f.close()

def shortest_path(g, node1_id, node2_id, max_hops=4):
    script = g.scripts.get("shortest_path")
    res = g.gremlin.execute(script, dict(node1_id=node1_id, node2_id=node2_id, hops=max_hops))
    if res:
        for path in res.results:
            print "----"
            for r in path.data:
                print _v2s(r)

def graph_info(g):
    script = g.scripts.get("graph_info")
    res = g.gremlin.execute(script)

    return res.results.next().data

def node_info(g, node_id):
    script = g.scripts.get("node_info")
    res = g.gremlin.execute(script, dict(node_id=node_id))
    return res.results.next().data

