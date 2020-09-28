
from werkzeug.exceptions import BadRequest

class ContentTypeNotJsonException(BadRequest):
    pass
    
class NotWellFormedJsonException(BadRequest):   
    pass

class WrongArgumentTypeException(TypeError):
	pass
	
class EntityNotFoundException(KeyError):
	pass
	
# I broke out WrongArgumentTypeException and EntityNotFoundException
# from TypeError and KeyError because, I found that my
# programming errors (when using stdlib or external lib functions)
# also resulted from TypeError and KeyError, and then our
# backend was interpreting those as the ones meant for the client
# when actually they're meant for me. So we'll catch these instead.
