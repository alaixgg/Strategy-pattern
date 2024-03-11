class ITax():
    def calculate_tax(self, money):
        pass

class TaxUE(ITax):
    def calculate_tax(self,money):
        return money * 0.2

class TaxUS(ITax):
    def calculate_tax(self,money):
        return money * 0.15
    

class Country:
    def __init__(self, tax_region: ITax) -> None:
        self.tax_region = tax_region
    
    def calculate_tax(self, money):
        return self.tax_region.calculate_tax(money)


class Spain(Country):
    def __init__(self,tax_region: ITax) :
        super().__init__(tax_region)


region = TaxUE()

spain = Spain(region)
print(spain.calculate_tax(10000))