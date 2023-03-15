
class MonostateSingleton:

    __state = {}

    def __new__(cls, *args, **kwds):
        obj = super(MonostateSingleton, cls).__new__(cls, *args, **kwds)
        obj.__dict__ = cls.__state
        return obj


m1 = MonostateSingleton()
print(f'm1 id [{id(m1)}]')
print(m1.__dict__)


m2 = MonostateSingleton()
print(f'm1 id [{id(m2)}]')
print(m2.__dict__)

m1.nome = "Um nome qualquer"

print(f'm1: {m1.__dict__}')
print(f'm2: {m2.__dict__}')