from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class HTTPTransaction(Node):

    element_type = "http_transaction"

    name = String(nullable=False)

class UserAgent(Node):

    element_type = "userAgent"

    name = String(nullable=False)

class URI(Node):

    element_type = "uri"

    name = String(nullable=False)

class Referrer(Relationship):
    label = "referrer"
    element_type = label
    
class HostedBy(Relationship):
    label = "hostedBy"
    element_type = label
    
class RequestedBy(Relationship):
    label = "requestedBy"
    element_type = label

class RequestedOf(Relationship):
    label = "requestedOf"
    element_type = label

class Requested(Relationship):
    label = "requested"
    element_type = label

    
