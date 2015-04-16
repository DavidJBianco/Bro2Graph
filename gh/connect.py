from bulbs.rexster import Graph, Config
from host import Host
from flow import Flow, Source, Dest, Contains
from dns import FQDN, DNSTransaction, LookedUp, Queried, Answer, QueriedServer, Resolved, ResolvedTo
from file import File, Transferred, ServedTo, ServedBy
from http import HTTPTransaction, URI, UserAgent, Referrer, HostedBy, RequestedBy, RequestedOf, Requested
from account import Account

DEFAULT_URI = "http://localhost:8182/graphs/hunting"

def Connect(uri=DEFAULT_URI):
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
    g.add_proxy("contains", Contains)
    g.add_proxy("dest", Dest)
    g.add_proxy("fqdn", FQDN)
    g.add_proxy("dnsTransaction", DNSTransaction)
    g.add_proxy("resolved", Resolved)
    g.add_proxy("answer", Answer)
    g.add_proxy("queried", Queried)
    g.add_proxy("queriedServer", QueriedServer)
    g.add_proxy("lookedUp", LookedUp)
    g.add_proxy("resolvedTo", ResolvedTo)
    g.add_proxy("file", File)
    g.add_proxy("transferred", Transferred)
    g.add_proxy("servedTo", ServedTo)
    g.add_proxy("servedBy", ServedBy)
    g.add_proxy("httpTransaction", HTTPTransaction)
    g.add_proxy("uri", URI)
    g.add_proxy("userAgent", UserAgent)
    g.add_proxy("account", Account)
    g.add_proxy("requested", Requested)
    # Load in our groovy scripts
    g.scripts.update("groovy/shortest_path.groovy")

    return g
