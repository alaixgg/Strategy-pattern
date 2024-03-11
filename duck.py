def IFLYBehavior():
    def fly():
        pass

class Duck: 
    def quack():
        print("Quack")

    def swim ():
        print("Camino")
    
    def display():
        print("Soy un pato")
    
    def fly():
        print("Estoy Volando")

class MallardDuck(Duck):
    def quack():
        print("QUAAAACK")

    def swim ():
        print("Corro")
    
    def display():
        print("Soy un pato real")

class RedHeadDuck(Duck):
    
    def display():
        print("Soy un pato de cabeza roja")

class RubberDuck(Duck):
    def display():
        print("Soy un pato de goma")

    def fly():
        print("No vuelo")