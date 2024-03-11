class ITaxBehavior:
    def calculate_taxes(self):
        pass

class TaxUS(ITaxBehavior):
    def calculate_taxes(self):
        print("tax del 15%")

class TaxEu(ITaxBehavior):
    def calculate_taxes(self):
        print("tax del 30%")

class Country: 
       def __init__(self, tax_region: ITaxBehavior) -> None:
           self.taxes = tax_region

       def perform_tax(self):
           self.taxes.calculate_taxes(self)

class Spain(Country):
    def __init__(self) -> None:
        super().__init__(TaxEu())

if __name__ == "__main__":
    
    region =TaxUS()
    
    Spain=Spain()
    Spain.perform_tax()