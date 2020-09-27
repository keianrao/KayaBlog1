
from werkzeug.exceptions import BadRequest

class ContentTypeNotJsonException(BadRequest):
    pass
    
class NotWellFormedJsonException(BadRequest):   
    pass
