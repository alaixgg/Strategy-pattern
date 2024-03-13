class singlenton:
    _instance = None

    def __new__(cls, *args, **kwarg):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwarg)
        return cls._instance
    
    def __init__(self):
        self.option_one ='opcion 1'
        self.option_two ='opcion 2'


singlenton_one = singlenton()
singlenton_two = singlenton()

print(singlenton_one)
print(singlenton_two)