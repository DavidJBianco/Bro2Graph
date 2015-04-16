#!/usr/bin/env python

from gh.connect import Connect
import sys
import re

g = Connect()

print "WARNING: This will DELETE ALL DATA in the graph.  Are you sure? (y/N) ",

answer = sys.stdin.readline()

# Do a case-insensitive match to see if the first char of the response is "y"
if re.match('y', answer, re.I):
    g.clear()
else:
    print "Graph data NOT DELETED."

    


