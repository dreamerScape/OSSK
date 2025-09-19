from abc import ABC, abstractmethod

class Medicine(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    @property
    @abstractmethod
    def quantity(self) -> int:
        pass
    @property
    @abstractmethod
    def price(self) -> float:
        pass
    
    @abstractmethod
    def requires_prescription(self) -> bool:
        pass
    @abstractmethod
    def storage_requirements(self) -> str:
        pass
    def total_price(self) -> float:
        return self.quantity * self.price

    def info(self) -> str:
        return f"Medicine Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Total: {self.total_price()}"
    
    

class Antibiotic(Medicine):
    def __init__(self, name: str, quantity: int, price: float):
        self._name = name
        self._quantity = quantity
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def price(self) -> float:
        return self._price

    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "8-15°С, темне місце"


class Vitamin(Medicine):
    def __init__(self, name: str, quantity: int, price: float):
        self._name = name
        self._quantity = quantity
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def price(self) -> float:
        return self._price

    def requires_prescription(self) -> bool:
        return False

    def storage_requirements(self) -> str:
        return "15-25°С, сухо"


class Vaccine(Medicine):
    def __init__(self, name: str, quantity: int, price: float):
        self._name = name
        self._quantity = quantity
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def price(self) -> float:
        return self._price

    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "2-8°С, холодильник"

    def total_price(self) -> float:
        return self.quantity * self.price * 1.1
