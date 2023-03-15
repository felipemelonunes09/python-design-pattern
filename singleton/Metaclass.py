
class MetaclassObject(type):

    def __call__(cls, *args, **kwds):
        print(f"Esses sao or agumentos: {args}")
        return type.__call__(cls, *args, **kwds)


class Object(metaclass=MetaclassObject):

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

obj = Object(43, 23)
print(obj)