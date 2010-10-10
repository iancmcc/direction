from json import JSONEncoder
from .interfaces import Serializable

class JSONSerializer(JSONEncoder):
    def default(self, o):
        if isinstance(o, Serializable):
            return o.serialize()
        return JSONEncoder.default(self, o)
