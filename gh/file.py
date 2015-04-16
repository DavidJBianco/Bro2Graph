from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class File(Node):

    element_type = "file"

    name = String(nullable=False)

class Transferred(Relationship):
    label = "transferred"
    element_type = label
    
class ServedTo(Relationship):
    label = "servedTo"
    element_type = label
    
class ServedBy(Relationship):
    label = "servedBy"
    element_type = label
    

    
