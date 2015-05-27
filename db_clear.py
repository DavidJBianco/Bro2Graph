#!/usr/bin/env python

from gh.connect import Connect

from optparse import OptionParser
import sys
import re

def parse_options() :
    parser = OptionParser()
    parser.add_option("-f", "--force", dest="force",default=False,
                      action="store_true",
                      help="Force clear the DB, without prompting for confirmation.")
    (options, args) = parser.parse_args()
    return(options, args)

### MAIN ###
(options, args) = parse_options()

g = Connect()

# don't prompt if we used --force
if options.force:
    g.clear()
else:
    print "WARNING: This will DELETE ALL DATA in the graph.  Are you sure? (y/N) ",

    answer = sys.stdin.readline()

    # Do a case-insensitive match to see if the first char of the response is "y"
    if re.match('y', answer, re.I):
        g.clear()
    else:
        print "Graph data NOT DELETED."

    


