#!/usr/bin/env python

from optparse import OptionParser
import sys

import gh

def parse_options() :
    parser = OptionParser()
    parser.add_option("-v", "--verbose", dest="verbose",default=False,
                      action="store_true",
                      help="Print more details about nodes and edges.")
    parser.add_option("-d", "--directed", dest="directed", default=False,
                      action="store_true",
                      help="Respect relationship direction when finding paths.")
    parser.add_option("-m", "--max_hops", dest="max_hops", default=4,
                      help="Max number of hops in path.")
    (options, args) = parser.parse_args()
    return(options, args)

#### MAIN ####

(options, args) = parse_options()

if len(args) != 2:
    print "ERROR: You must specify both the beginning and ending node IDs"
    sys.exit(-1)

g = gh.connect.Connect()

res = gh.util.shortest_path(g, args[0], args[1],
                            directed=options.directed,
                            max_hops=options.max_hops)

if res:
    for r in res:
        print gh.util._v2s(r,verbose=options.verbose),
else:
    print "No path."
    
