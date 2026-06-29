# Base Class
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days

    def display(self, days):
        print(f"Model: {self.model}")
        print(f"Rental Rate: ₹{self.rental_rate}/day")
        print(f"Total Rental Cost ({days} days): ₹{self.calculate_rental(days)}")


# Subclass 1 - Car
class Car(Vehicle):
    def __init__(self, model, rental_rate, ac_charge=500):
        super().__init__(model, rental_rate)
        self.ac_charge = ac_charge

    def calculate_rental(self, days):
        return (self.rental_rate + self.ac_charge) * days


# Subclass 2 - Bike
class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_charge=100):
        super().__init__(model, rental_rate)
        self.helmet_charge = helmet_charge

    def calculate_rental(self, days):
        return (self.rental_rate + self.helmet_charge) * days


# Subclass 3 - Truck
class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_charge=1000):
        super().__init__(model, rental_rate)
        self.load_charge = load_charge

    def calculate_rental(self, days):
        return (self.rental_rate + self.load_charge) * days


# Testing
print("=== Car Rental ===")
car = Car("Swift", 1000, ac_charge=500)
car.display(3)

print("\n=== Bike Rental ===")
bike = Bike("Splendor", 300, helmet_charge=100)
bike.display(2)

print("\n=== Truck Rental ===")
truck = Truck("Tata407", 2000, load_charge=1000)
truck.display(5)

print("\n=== Polymorphism - All Vehicles ===")
vehicles = [(car, 3), (bike, 2), (truck, 5)]
for v, d in vehicles:
    print(f"{v.model} => ₹{v.calculate_rental(d)}")