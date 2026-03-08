#Create a module for further uses in food_types
from abc import ABC, abstractmethod

class FoodItem(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @abstractmethod #Setting a default
    def get_category(self):
        pass

    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price