from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class Account(Node):

    element_type = "account"

    name = String(nullable=False)
    color = String(default="#00FFFF")
    
class Requested(Relationship):
    label = "requested"
    element_type = label

class Uses(Relationship):
    label = "uses"
    element_type = label

    
    

    
