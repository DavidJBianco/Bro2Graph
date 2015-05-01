from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class FQDN(Node):

    element_type = "fqdn"

    name = String(nullable=False)
    color = String(default="#8CBC1C")
    
class DNSTransaction(Node):
    element_type = "dnsTransaction"

    name = String(nullable=False)
    color = String(default="#FFBF56")
    
class Resolved(Relationship):
    label = "resolved"
    element_type = label

class Answer(Relationship):
    label = "answer"
    element_type = label
    
class Queried(Relationship):
    label = "queried"
    element_type = label

class QueriedServer(Relationship):
    label = "queriedServer"
    element_type = label

class LookedUp(Relationship):
    label = "lookedUp"
    element_type = label

class ResolvedTo(Relationship):
    label = "resolvedTo"
    element_type = label
    
