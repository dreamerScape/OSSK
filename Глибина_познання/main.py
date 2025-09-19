
from models import Bicycle, Bus, Car, ElectricCar


vehicles = [
    Car("Toyota", 90, 5),
    Bus("Mercedes", 70, 20),
    Bicycle("BMX", 25, 1),
    ElectricCar("Tesla", 120, 5)
]

distance = 100  
price_per_unit = 2.5

for v in vehicles:
    print(f"Name: {v.name}")
    time = v.move(distance)
    print(f"Time {distance} km: {time} hour")
    fuel = v.fuel_consumption(distance)
    print(f"Fule cons: {fuel}")
    cost = v.calculate_cost(distance, price_per_unit)
    print(f"total cost: {cost}")
    print("-" * 30)