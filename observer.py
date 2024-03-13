class Isubcriber:
    def upgate (self, message):
        pass 

class Notifier:

    def __init__(self) -> None:
        self._subcriber = []

    def attach(self, subcriber:Isubcriber):
        if subcriber not in self._subcriber:
            self._subcriber.append(subcriber)
        
    def detach(self, subcriber:Isubcriber):
        if subcriber in self._subcriber:
            self._subcriber.remove(subcriber)

    def notify(self, message):
        for subcriber in self._subcriber:
            subcriber.upgate(message)

class subcriber(Isubcriber):
    def __init__(self, name) -> None:
        super().__init__()
        self.__name = name

    def upgate(self, message):
        print(f "{self.__name} recibio el mensaje: {}")

if __name__ == '__main__':
    notifier = Notifier()
    subcriber_one = subcriber("11")
    subcriber_two = subcriber("22")

    notifier.attach(subcriber_one)
    notifier.attach(subcriber_two)

    notifier.notify("ha ocurrido un evento")

    notifier.detach(subcriber_one)
    notifier.notify("se ha eliminado a 11")
    