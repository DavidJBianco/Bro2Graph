from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class DNS(Node):

    element_type = "dns"

    name = String(nullable=False)

class Resolved(Relationship):
    label = "resolved"
    element_type = "resolved"

    
    
