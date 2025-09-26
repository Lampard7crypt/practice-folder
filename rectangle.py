class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def car_version(self):
        return f"{self.brand} from {self.year}"
    def move(self):
        return f"Your {self.brand} started moving"
    def stop(self):
        return f"Your {self.brand} stopped"
class Components(Car):

    def __init__(self, brand, year, engine_type):
        self.brand = brand
        self.year = year
        self.engine_type = engine_type
    def engine(self):
        return f"Your {self.brand} from {self.year} has {self.engine_type}"
    
class Externals(Car):
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
    def car_color(self):
        return f"{self.color}? Nice color there!😎"
    

car = Car("Audi", 2019)
print(car.car_version)
print(car.move)
print(car.stop)
