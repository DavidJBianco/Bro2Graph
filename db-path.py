#!/usr/bin/env python

from optparse import OptionParser
import sys

import gh

def parse_options() :
    parser = OptionParser()
    parser.add_option("-v", "--verbose", dest="verbose",default=False,
                      action="store_true",
                      help="Print more details about nodes and edges.")
    (options, args) = parser.parse_args()
    return(options, args)

#### MAIN ####

(options, args) = parse_options()

if len(args) != 2:
    print "ERROR: You must specify both the beginning and ending node IDs"
    sys.exit(-1)

g = gh.connect.Connect()

res = gh.util.shortest_path(g, args[0], args[1])

if res:
    for r in res:
        print gh.util._v2s(r,verbose=options.verbose),
else:
    print "No path."
    
