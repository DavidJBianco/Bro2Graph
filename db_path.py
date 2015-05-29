#!/usr/bin/env python

from optparse import OptionParser
import sys
import re

import gh

def parse_options() :
    parser = OptionParser()
    parser.add_option("-v", "--verbose", dest="verbose",default=False,
                      action="store_true",
                      help="Print more details about nodes and edges.")
    parser.add_option("-d", "--directed", dest="directed", default=False,
                      action="store_true",
                      help="Respect relationship direction when finding paths.")
    parser.add_option("-m", "--max_hops", dest="max_hops", default=5,
                      help="Max number of hops in path.")
    (options, args) = parser.parse_args()
    return(options, args)

#### MAIN ####

(options, args) = parse_options()

if len(args) != 2:
    print "ERROR: You must specify both the beginning and ending nodes."
    sys.exit(-1)

g = gh.connect.Connect()

src = args[0]
dst = args[1]

# Look up the source ID, if we gave a name
if re.match("\d+$", dst):
    print "Looking up by destination vertex ID"
    lookup = gh.util.shortest_path
else:
    print "Looking up by destination vertex type"
    lookup = gh.util.shortest_path_to_type

res = lookup(g, src, dst,
             directed=options.directed,
             max_hops=options.max_hops)

if res:
    for r in res:
        print gh.util._v2s(r,verbose=options.verbose),
else:
    print "No path."
    
