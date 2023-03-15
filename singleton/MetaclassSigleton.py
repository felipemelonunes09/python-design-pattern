
class MetaSingleton(type):

    __instances = {}

    def __call__(cls, *args: any, **kwds: any) -> any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwds)
        return cls.__instances[cls]

class Object(metaclass=MetaSingleton):
    pass

obj1 = Object()
obj2 = Object()

print(f"obj1 {id(obj1)}")
print(f"obj2 {id(obj2)}")

print("the same id")