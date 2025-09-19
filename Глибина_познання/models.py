from abc import ABC, abstractmethod

class Transport(ABC):
    @property
    @abstractmethod
    def name(self)->str:
        pass

    @property
    @abstractmethod
    def speed(self)->int:
        pass

    @property
    @abstractmethod
    def capacity(self)->int:
        pass

    @abstractmethod
    def move(self, distance: int)->float:
        pass

    @abstractmethod
    def fuel_consumption(self, distance: int, passengers: int = 1) -> float:
        pass

    @abstractmethod
    def info(self)->str:
        pass

    @abstractmethod
    def calculate_cost(self, distance: int, price_per_unit: float) -> float:
        pass

class Car(Transport):
    def __init__(self, name: str, speed: float, capacity: int):
        self._name = name
        self._speed = speed
        self._capacity = capacity

    @property
    def name(self)->str:
        return self._name

    @property
    def speed(self)->int:
        return self._speed

    @property
    def capacity(self)->int:
        return self._capacity

    def move(self, distance: int)->float:
        return distance / self.speed

    def fuel_consumption(self, distance: int, passengers: int = 1) -> float:
        return distance * 0.07

    def info(self) -> str:
        return f"AUTO: {self.name}, speed: {self.speed}, capacity: {self.capacity}"

    def calculate_cost(self, distance: int, price_per_unit: float, passengers: int = 1) -> float:
        fuel = self.fuel_consumption(distance, passengers)
        return fuel * price_per_unit


class Bus(Transport):
    def __init__(self, name: str, speed: float, capacity: int):
        self._name = name
        self._speed = speed
        self._capacity = capacity

    @property
    def name(self)->str:
        return self._name

    @property
    def speed(self)->int:
        return self._speed

    @property
    def capacity(self)->int:
        return self._capacity

    def move(self, distance: int)->float:
        return distance / self.speed

    def fuel_consumption(self, distance: int, passengers: int = 1) -> float:
        if passengers > self.capacity:
            print("Перевантажено!")
        return distance * 0.15

    def info(self) -> str:
        return f"Bus: {self.name}, speed: {self.speed}, capacity: {self.capacity}"

    def calculate_cost(self, distance: int, price_per_unit: float, passengers: int = 1) -> float:
        fuel = self.fuel_consumption(distance, passengers)
        return fuel * price_per_unit


class Bicycle(Transport):
    def __init__(self, name: str, speed: float = 20, capacity: int = 1):
        capped_speed = min(speed, 20)
        self._name = name
        self._speed = capped_speed
        self._capacity = capacity

    @property
    def name(self)->str:
        return self._name

    @property
    def speed(self)->float:
        return self._speed

    @property
    def capacity(self)->int:
        return self._capacity

    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int, passengers: int = 1) -> float:
        return 0

    def info(self) -> str:
        return f"Bicycle: {self.name}, speed: {self.speed}, capacity: {self.capacity}"

    def calculate_cost(self, distance: int, price_per_unit: float, passengers: int = 1) -> float:
        fuel = self.fuel_consumption(distance, passengers)
        return fuel * price_per_unit


class ElectricCar(Car):
    def __init__(self, name: str, speed: float, capacity: int):
        self._name = name
        self._speed = speed
        self._capacity = capacity

    @property
    def name(self)->str:
        return self._name

    @property
    def speed(self)->int:
        return self._speed

    @property
    def capacity(self)->int:
        return self._capacity

    def fuel_consumption(self, distance: int, passengers: int = 1) -> float:
        return 0

    def battery_usage(self, distance: int):
        return distance * 0.2

    def info(self) -> str:
        return f"ElectricCar: {self.name}, speed: {self.speed}, capacity: {self.capacity}"

    def calculate_cost(self, distance: int, price_per_unit: float, passengers: int = 1) -> float:
        fuel = self.fuel_consumption(distance, passengers)
        return fuel * price_per_unit

