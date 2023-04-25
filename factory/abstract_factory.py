from abc import ABCMeta, abstractmethod


# abstract Factory

class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass
    
    @abstractmethod
    def criar_pizza(self):
        pass


# concreto factory A

class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaCamarao()

# concreto factory B

class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocolis()

    def criar_pizza(self):
        return PizzaBolonha()

# abstract produto A

class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, PizzaVeg):
        pass

# abstract produto B

class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, Pizza):
        pass

# produto concreto

class PizzaMandioca(PizzaVeg):

    def preparar(self, PizzaVeg):
        print(f"prearando pizza de mandioca do tipo {type(PizzaVeg).__name__}")


class PizzaCamarao(Pizza):

    def preparar(self, Pizza):
        print(f"prearando pizza de mandioca do tipo {type(Pizza).__name__}")


class PizzaBrocolis(PizzaVeg):

    def preparar(self, PizzaVeg):
        print(f"prearando pizza de brocolis do tipo {type(PizzaVeg).__name__}")

class PizzaBolonha(Pizza):

    def preparar(self, Pizza):
        print(f"prearando pizza de brocolis do tipo {type(Pizza).__name__}")


## cliente

class Pizarria:

    def fazer_pizzas(self):

        for factory in [PizzaBrasileira(), PizzaItaliana()]:

            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg()

            self.pizza.preparar(self.pizza)
            self.pizza_veg.preparar(self.pizza_veg)

pizarria = Pizarria()
pizarria.fazer_pizzas()