#This is main file
from food_base import FoodItem      
from food_types import Burger, Drink, Fries  
from order_calculator import calculate_total  
#Setting the value of the food
cheeseburger = Burger("Cheese Burger", 5.99)
cola = Drink("Coca Cola", 1.99)
curly_fries = Fries("Curly Fries", 2.49)
#Set a order list
order = [cheeseburger, cola, curly_fries]
# Calculate and output the total cost
calculate_total(order)