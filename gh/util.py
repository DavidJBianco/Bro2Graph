#!/usr/bin/env python

def _v2s(v, verbose=False):
    if not "_type" in v:
        return "-"
    elif v["_type"] == "vertex":
        if verbose:
            return "v[%s][%s %s]" % (v["_id"], v["element_type"], v["name"])
        else:
            return "v[%s]" % v["_id"]
    elif v["_type"] == "edge":
        if verbose:
            return "e[%s][%s-%s->%s]" % (v["_id"], v["_outV"], v["element_type"], v["_inV"])
        else:
            return "e[%s][%s-%s->%s]" % (v["_id"], v["_outV"], v["element_type"], v["_inV"])
    else:
        return "[??]"

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

def shortest_path(g, node1_id, node2_id, max_hops=4, directed=False):
    '''
    Calls a Groovy script to compute the shortest path between two
    nodes that is less than or equal to "max_hops" long. In the event
    that there are multiple paths of the same length, it only returns
    one of them.  Which one it returns is undefined. If the "directed"
    attribute is True, the function will follow relationships only in
    the direction in which they occur on the graph. If set to False,
    it will find paths regardelss of the direction of the
    relationships.

    Return value is either a list of nodes and edges, or None if no path
    was found.

    '''
    script = g.scripts.get("shortest_path")
    res = g.gremlin.execute(script, dict(node1_id=node1_id, node2_id=node2_id, hops=max_hops, directed=directed))
    if res:
        lst = list(res.results)
        # Results will be a list-of-lists. If there are any results, return
        # the first list.
        if len(lst) > 0:
            return lst[0].data
    # If we got here, there were no results, so we couldn't find a path.
    return None

def shortest_path_to_type(g, node1_id, node2_type, max_hops=4, directed=False):
    '''
    Calls a Groovy script to compute the shortest path between two
    nodes that is less than or equal to "max_hops" long, where the destination
    node is any node of the type specified in "node2_type". In the event
    that there are multiple paths of the same length, it only returns
    one of them.  Which one it returns is undefined. If the "directed"
    attribute is True, the function will follow relationships only in
    the direction in which they occur on the graph. If set to False,
    it will find paths regardelss of the direction of the
    relationships.

    Return value is either a list of nodes and edges, or None if no path
    was found.

    '''
    script = g.scripts.get("shortest_path_to_type")
    res = g.gremlin.execute(script, dict(node1_id=node1_id, node2_type=node2_type, hops=max_hops, directed=directed))
    if res:
        lst = list(res.results)
        # Results will be a list-of-lists. If there are any results, return
        # the first list.
        if len(lst) > 0:
            return lst[0].data
    # If we got here, there were no results, so we couldn't find a path.
    return None

def graph_info(g):
    script = g.scripts.get("graph_info")
    res = g.gremlin.execute(script)

    return res.results.next().data

def node_info(g, node_id):
    script = g.scripts.get("node_info")
    res = g.gremlin.execute(script, dict(node_id=node_id))
    return res.results.next().data

def edge_list(g, node1_id, node2_id, edge_type):
    script = g.scripts.get("edge_list")
    res = g.gremlin.query(script, dict(node1_id=node1_id, node2_id=node2_id, edge_type=edge_type))
    return res
