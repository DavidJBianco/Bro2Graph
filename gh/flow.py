from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class Flow(Node):

    element_type = "flow"
    name = String(nullable=False)
    color = String(default="#5B87F2")
    
class Source(Relationship):
    label = "source"
    element_type = label
    
class Dest(Relationship):
    label = "dest"
    element_type = label

class ConnectedTo(Relationship):
    label = "connectedTo"
    element_type = label
    
class Contains(Relationship):
    label = "contains"
    element_type = label


