from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class Account(Node):

    element_type = "account"

    name = String(nullable=False)

class Requested(Relationship):
    label = "requested"
    element_type = label

    

    
