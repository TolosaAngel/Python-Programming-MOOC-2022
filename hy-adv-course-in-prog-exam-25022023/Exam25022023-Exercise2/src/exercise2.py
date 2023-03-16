class Driver:
    def __init__(self, name: str, year_of_birth: int, height: int, weight: int):
        self.name = name
        self.year_of_birth = year_of_birth
        self.height = height
        self.weight = weight

    def __str__(self):
        return (f"Driver(name = {self.name}, " + f"year_of_birth = {self.year_of_birth}, " + f"height = {self.height}, weight = {self.weight})")

class RallyCar:
    def __init__(self, make: str, top_speed: int, driver: Driver):
        self.make = make
        self.top_speed = top_speed
        self.driver = driver

    def __str__(self):
        return (f"RallyCar(make = {self.make}, " + f"top_speed = {self.top_speed}, " + f"driver = {self.driver})")
    
def fastest_cars(cars: list, speed: int):
    return [car.make for car in cars if car.top_speed > speed]

def drivers_of_make(cars: list, make: str):
    return [car.driver.name for car in cars if car.make == make]

def youngest_and_oldest_driver(drivers: list):
    list_by_age = sorted(drivers, key = lambda driver: driver.year_of_birth)

    oldest_driver = list_by_age[0].name
    youngest_driver = list_by_age[-1].name

    return (youngest_driver, oldest_driver)

def by_speed(cars: list):
    return sorted(cars, key = lambda car: car.top_speed)