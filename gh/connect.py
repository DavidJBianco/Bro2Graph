from bulbs.rexster import Graph, Config
from host import Host
from flow import Flow, Source, Dest
from dns import FQDN, DNSTransaction, LookedUp, Queried, Answer, QueriedServer, Resolved, ResolvedTo

URI = "http://localhost:8182/graphs/hunting"

def Connect(uri=URI):
    """
    Establishes a connection to the graph database backend.  It also does 
    a few standard tasks to set up the models and server side scripts we
    depend on, so every utility that calls Connect() has a consistent 
    environment.

    Returns a Graph() object.

    Example:

        g = Connect()  # Connect using the standard default database info
        g = Connect("http://localhost:8182/graphs/myDB") # Use a custom DB
    """
    config = Config(uri)
    g = Graph(config)
    
    # Set up the node and relationship proxies
    g.add_proxy("host", Host)
    g.add_proxy("flow", Flow)
    g.add_proxy("source", Source)
    g.add_proxy("dest", Dest)
    g.add_proxy("fqdn", FQDN)
    g.add_proxy("dnsTransaction", DNSTransaction)
    g.add_proxy("resolved", Resolved)
    g.add_proxy("answer", Answer)
    g.add_proxy("queried", Queried)
    g.add_proxy("queriedServer", QueriedServer)
    g.add_proxy("lookedUp", LookedUp)
    g.add_proxy("resolvedTo", ResolvedTo)
    
    # Load in our groovy scripts
    g.scripts.update("groovy/shortest_path.groovy")

    return g
