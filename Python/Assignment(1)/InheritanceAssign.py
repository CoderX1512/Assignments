# Let's create a base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


# Let's create the child classes
class Car(Vehicle):
    def __init__(self, make, model, price):
        super().__init__(make, model)
        self.price = price

    def compare(self):
        if self.price <= 2000000:
            print(f"The car {self.make} {self.model} is priced at {self.price} is affordable")
        else:
            print(f"The car {self.make} {self.model} is priced at {self.price} is expensive")


class Motorcycle(Vehicle):
    def __init__(self, maker, model, mileage):
        super().__init__(maker, model)
        self.mileage = mileage

    def compare_mil(self):
        if self.mileage >= 60:
            print(f"The motorcycle {self.make} {self.model} provides very good mileage")
        elif 40 <= self.mileage < 60:
            print(f"The motorcycle {self.make} {self.model} provides decent mileage")
        else:
            print(f"The motorcycle {self.make} {self.model} provides average mileage")


# Creating instances of derived  class
car1 = Car("Audi", "Q3", 5000000)
car2 = Car("Mercedes-Benz", "A-Class Limousine", 4500000)
car3 = Car("Mahindra", "XUV700", 1900000)

car1.compare()
car2.compare()
car3.compare()

bike1 = Motorcycle("Bajaj", "CT100B", 80)
bike2 = Motorcycle("Bajaj", "CT100B", 80)
bike3 = Motorcycle("TVS", "Apache RTR 160 4V", 35)
