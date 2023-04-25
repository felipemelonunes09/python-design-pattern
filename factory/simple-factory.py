from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("wolf wolf")


class Cat(Animal):
    def talk(self):
        print("meow meow")


class Factory:
    def create_talk_animal(self, _type):
        return eval(_type)().talk()
				#return evel(_type)() ## you could return the object

fab = Factory()
animal = fab.create_talk_animal(input("type [Dog or Cat]: "))