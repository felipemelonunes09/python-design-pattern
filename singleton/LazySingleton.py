
class Singleton(object):

    __instance = None

    def __init__(self) -> None:
        if not Singleton.__instance:
            print("O metodo __init__ foi chamado...")
        else:
            print(f'A instancia foi criado: {self.get_instance()}')

    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton() # a classe e inicializada mas o objeto nao e criado

print(f"Objeto e criado agora: {Singleton.get_instance()}")

s2 = Singleton() #instancia ja criada

print(f'instancia 1: {id(s1.get_instance())}')
print(f'instancia 1: {id(s2.get_instance())}')

