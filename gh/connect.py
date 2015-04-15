from bulbs.rexster import Graph, Config
from host import Host
from flow import Flow, Source, Dest
from dns import DNS, Resolved

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
    g.add_proxy("dns", DNS)
    g.add_proxy("resolved", Resolved)
    
    # Load in our groovy scripts
    g.scripts.update("groovy/shortest_path.groovy")

    return g
