#creamos la clase que maneja sinlgeton 

class singleton:
    _intance= None

    def __init__(self) -> None:
        if singleton._intance is not None:
            raise Exception("Clase ya instanciada")

        singleton._intance = self
        self.option_one ='opcion 1'
        self.option_two ='opcion 2'

    @staticmethod
    def get_instance():
        if singleton._intance is None:
            singleton._intance = singleton()
        
        return singleton._intance
    
singleton_one = singleton.get_instance()
singleton_two = singleton.get_instance()

print(singleton_one)
print(singleton_two)

singleton_one.option_one = 'prueba clase'

print(singleton_one)
print(singleton_one)