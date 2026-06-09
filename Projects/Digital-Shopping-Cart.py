# 1. Initialize variables to keep track of our totals
subtotal = 0
invoice_items = "" # We will add each product's text to this string

print("--- Digital Shopping Cart ---")
print("Please enter the details for 5 products.\n")

# 2. Use a simple loop to collect input for 5 products
for i in range(1, 6):
    name = input(f"Enter Product {i} Name: ")
    quantity = int(input(f"Enter Quantity for {name}: "))
    price = float(input(f"Enter Price for {name}: "))
    
    # Calculate the total for this specific item
    item_total = quantity * price
    
    # Add this item's total to our running subtotal
    subtotal += item_total
    
    # Add the formatted text to our invoice_items string for later
    invoice_items += f"{name} \t {quantity} * {price} = {item_total}\n"

# 3. Calculate GST (18%) and the Grand Total
gst = subtotal * 0.18
grand_total = subtotal + gst

# 4. Extension: Apply Discount based on the Subtotal
discount_amount = 0

if subtotal > 50000:
    discount_amount = grand_total * 0.10  # 10% discount
elif subtotal > 25000:
    discount_amount = grand_total * 0.05  # 5% discount

# Calculate the final bill after any discounts
final_bill = grand_total - discount_amount

# 5. Display the Final Output
print("\n========== INVOICE ==========")
print(invoice_items.strip()) 
print("-----------------------------")
print(f"Subtotal : {subtotal}")
print(f"GST (18%): {gst}")
print(f"Total    : {grand_total}")

# Only show the discount section if they actually earned one
if discount_amount > 0:
    print("\n--- Extension ---")
    print(f"Discount Applied : -{discount_amount}")
    print(f"Final Bill       : {final_bill}")
print("=============================")