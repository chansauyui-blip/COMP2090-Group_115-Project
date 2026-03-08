#Create a module to set the food types
from food_base import FoodItem #Imported the file food_base to this file

class Burger(FoodItem):
    def get_category(self):
        return "Burger"

class Drink(FoodItem):
    def get_category(self):
        return "Drink"

class Fries(FoodItem):
    def get_category(self):
        return "Fries"