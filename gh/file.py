from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class File(Node):

    element_type = "file"

    name = String(nullable=False)

class Transferred(Relationship):
    label = "transferred"
    element_type = label
    
class RequestedBy(Relationship):
    label = "requestedBy"
    element_type = label
    
class RequestedOf(Relationship):
    label = "requestedOf"
    element_type = label
    

    
