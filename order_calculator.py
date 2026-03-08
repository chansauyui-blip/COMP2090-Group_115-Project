#Create a module for calculating the total cost
def calculate_total(order_items):
    total = 0.0

    for item in order_items:
        print(f"- {item.get_category()}: {item.get_name()} (${item.get_price():.2f})")
        total += item.get_price()
    print(f"\nThe total cost is:${total:.2f}")