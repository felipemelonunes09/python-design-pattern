
from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):

    @abstractmethod
    def __repr__(self):
        pass

class SecaoPessoal(Secao):

    def __repr__(self):
        return "Secao Pessoal"

class SecaoAlbum(Secao):

    def __repr__(self):
        return "Secao album"


class SecaoProjeto(Secao):

    def __repr__(self):
        return "Secao Projeto"

class SecaoPublicacao(Secao):

    def __repr__(self):
        return "Secao Publicacao"


class Perfil(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes

    def add_secoes(self, secao):
        self.secoes.append(secao)

class Linkedin(Perfil):

    def criar_perfil(self):
        self.add_secoes( SecaoPessoal() )
        self.add_secoes( SecaoProjeto() )
        self.add_secoes( SecaoPublicacao() )

class Facebook(Perfil):

    def criar_perfil(self):
        self.add_secoes(SecaoPessoal())
        self.add_secoes(SecaoAlbum())


rede_social = input("[Linkedin ou Facebook] ")
perfil = eval(rede_social)()

print(type(perfil).__name__)
print(perfil.get_secoes())


