


class SanityCheker:

    __instances = None

    def __new__(cls, *args, **kwd):
        if not SanityCheker.__instances:
            SanityCheker.__instances = super(SanityCheker, cls).__new__(cls, *args, **kwd)
        return SanityCheker.__instances

    def __init__(self) -> None:
        self.__servidores = []

    def check_server(self, srv):
        print(f"checking the {self.__servidores[srv]}")

    def add_server(self):
        self.__servidores.append("SERVIDOR 1")
        self.__servidores.append("SERVIDOR 2")
        self.__servidores.append("SERVIDOR 3")
        self.__servidores.append("SERVIDOR 4")

    def change_server(self):
        self.__servidores.pop()
        self.__servidores.append("servidor 5")


sdc1 = SanityCheker()
sdc2 = SanityCheker()


sdc1.add_server()
print("task cheking sanity A...")

for s in range(4):
    sdc1.check_server(s)

sdc2.change_server()
print("task cheking sanity B...")
    
for s in range(4):
    sdc2.check_server(s)
