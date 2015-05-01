from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class Host(Node):

    element_type = "host"

    name = String(nullable=False)
    color = String(default="#DA456B")
    
