#!/usr/bin/env python

from gh.connect import Connect

g = Connect()

script = g.scripts.get("shortest_path:shortest_path")
params = dict(v1=g.host.index.lookup(name="172.16.112.194").next()._id,
              v2=g.host.index.lookup(name="196.37.75.158").next()._id,
              hops=4)
path = g.gremlin.query(script, params)

for p in path:
    print p.data()
    


