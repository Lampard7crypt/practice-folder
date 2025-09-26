class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def drive(self):
        return f"I'm driving a {self.brand} from the year {self.year}"
    
car = Car("Mercedez", 2024)
print(car.drive())

class ElectricCar(Car):
    def __init__(self, battery_life):
        self.batterylife = battery_life
    def type(self):
        return 