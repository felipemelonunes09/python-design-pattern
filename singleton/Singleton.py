

class Singleton(object):

    # metodo chamado antes do metodo __init__ 
    # metodo usado para criar um novo objeto
    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Criando o objeto {cls.instance}')
        
        return cls.instance


s1 = Singleton()
print(f'instancia 1: {id(s1)}')
    
s2 = Singleton()
print(f'instancia 1: {id(s2)}')

print("se as instancias tiverem o mesmo ID entao o padrao esta funcionando corretamente")
