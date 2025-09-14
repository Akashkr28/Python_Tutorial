class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai.")

class MasalaChai(BaseChai): # Inheritance
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


class ChaiShop:
    chai_cls = BaseChai  # Default chai class

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop") # Composition
        self.chai.prepare()

class FancyChaiShop(ChaiShop): # Inheritance
    chai_cls = MasalaChai  # Shadowing the class attribute


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()