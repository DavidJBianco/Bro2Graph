from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class HTTPTransaction(Node):

    element_type = "http_transaction"
    name = String(nullable=False)
    color = String(default="#5FBD71")
    
class UserAgent(Node):

    element_type = "userAgent"
    name = String(nullable=False)
    color = String(default="#BE844A")
    
class URI(Node):

    element_type = "uri"
    name = String(nullable=False)
    color = String(default="#71985E")
    
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

class IdentifiedBy(Relationship):
    label = "identifiedBy"
    element_type = label

class Agent(Relationship):
    label = "agent"
    element_type = label

class Sent(Relationship):
    label = "sent"
    element_type = label

class Received(Relationship):
    label = "received"
    element_type = label

    
