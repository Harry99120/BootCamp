class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
product_data = [
    ("Laptop", 1200.00, 5),
    ("Smartphone", 800.00, 10),
    ("Headphones", 150.00, 20)
]

inventory = []
for name, price, quantity in product_data:
    item = Product(name, price, quantity)
    inventory.append(item)

grand_total = 0

print("--- Inventory Report ---")
for product in inventory:
    product_total = product.total_value()
    grand_total += product_total
    
    print(f"Product: {product.name} | Total Value: ${product_total:.2f}")

print("------------------------")
print(f"Grand Total Inventory Value: ${grand_total:.2f}")