class ICharacher:
    def player(self):
        pass


class solado(ICharacher):
    def attack(self):
        print("golpe")

    def move(self):
        print("trotar")

class caballero(ICharacher):

    def attack(self):
        print("lanza")

    def move(self):
        print("corre")

class arquero(ICharacher):

    def attack(self):
        print("flecha")

    def move(self):
        print("camina")

class player:
    def __init__(self, campeon: ICharacher) -> None:
        self.player = campeon
    
    def attack(self):
        return self.player.attack(self)
    def move (self):
        return (self.player.move(self))
