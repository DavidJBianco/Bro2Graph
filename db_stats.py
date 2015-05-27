#!/usr/bin/env python

# Our interface to the GraphDB
from bulbs.rexster import Graph, Config, DEBUG

# Our own modules
from gh.connect import Connect
from gh.util import graph_info

def graph_stats (g):
    info = graph_info(g)

    print
    print "**** Graph Stats"
    print
    print "  **** Totals"
    print "  %15s\t%d" % ("Vertices", info["numv"])
    print "  %15s\t%d" % ("Edges", info["nume"])
    print
    print "  **** Vertices by type:"
    for v in info["vinfo"]:
        print "  %15s\t%d" % (v, info["vinfo"][v])
    print
    print "  **** Edges by type:"
    for e in info["einfo"]:
        print "  %15s\t%d" % (e, info["einfo"][e])

if __name__ == "__main__":
    g = Connect()

    graph_stats(g)
