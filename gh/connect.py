from bulbs.rexster import Graph, Config
from host import Host
from flow import Flow, Source, Dest, Contains, ConnectedTo
from dns import FQDN, DNSTransaction, LookedUp, Queried, Answer, QueriedServer, Resolved, ResolvedTo
from file import File, Transferred, SentTo, SentBy
from http import HTTPTransaction, URI, UserAgent, Referrer, HostedBy, RequestedBy, RequestedOf, IdentifiedBy, Agent, Sent, Received
from account import Account, Requested

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
    g.add_proxy("connectedTo", ConnectedTo)
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
    g.add_proxy("sentTo", SentTo)
    g.add_proxy("sentBy", SentBy)
    g.add_proxy("httpTransaction", HTTPTransaction)
    g.add_proxy("uri", URI)
    g.add_proxy("userAgent", UserAgent)
    g.add_proxy("requestedBy", RequestedBy)
    g.add_proxy("requestedOf", RequestedOf)
    g.add_proxy("hostedBy", HostedBy)
    g.add_proxy("identifiedBy", IdentifiedBy)
    g.add_proxy("agent", Agent)
    g.add_proxy("sent", Sent)
    g.add_proxy("received", Received)
    g.add_proxy("account", Account)
    g.add_proxy("requested", Requested)
    # Load in our groovy scripts
    g.scripts.update("groovy/gremlin.groovy")
    return g
