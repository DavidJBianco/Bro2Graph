#!/usr/bin/env python

from gh.connect import Connect
import gh

from GephiStreamer import Node, Edge, GephiStreamerManager

from random import choice

def display_graph(t, nodes, edges):

    if nodes != None:
        print "*** Graphing Nodes"
        for n in nodes:
            node_temp = Node(n._id)

            properties = n.map()
            for key in properties:
                node_temp.property[key] = properties[key]

            node_temp.property["colour"] = node_temp.property["color"]
            node_temp.property["label"] = node_temp.property["name"]
            t.add_node(node_temp)

    if edges != None:
        print "*** Graphing Edges"
        for e in edges:
            src = e._outV
            dst = e._inV
            edge_temp = Edge(src, dst, directed=True)

            properties = e.map()
            for key in properties:
                edge_temp.property[key] = properties[key]
            
            t.add_edge(edge_temp)

    t.commit()

def display_graph_from_list(t, l=None):
    if l == None:
        return

    for element in l:
        if element["_type"] == "vertex":
            node_temp = Node(element["_id"])

            for key in element:
                node_temp.property[key] = element[key]

            node_temp.property["label"] = node_temp.property["name"]
            node_temp.property["colour"] = node_temp.property["color"]

            t.add_node(node_temp)
        elif element["_type"] == "edge":
            src = element["_outV"]
            dst = element["_inV"]
            edge_temp = Edge(src, dst, directed=True)

            for key in element:
                edge_temp.property[key] = element[key]

            t.add_edge(edge_temp)

    t.commit()

if __name__ == "__main__":
    g = Connect()
    t = GephiStreamerManager()

    print "Getting nodes..."
    nodes = g.V
    print "Getting edges..."
    edges = g.E

    display_graph(t, g.V, g.E)

    
