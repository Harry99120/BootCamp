def simple_calculator():
    """
    A simple calculator that accepts multiple numbers from the user
    and performs arithmetic operations on them.
    """
    numbers = []
    
    print("=== Simple Calculator ===")
    print("Enter numbers one by one. Press Enter without typing a number to stop.")
    print()
    
    # Collect numbers from user
    while True:
        try:
            user_input = input(f"Enter number {len(numbers) + 1}: ").strip()
            
            # If user presses Enter without input, stop collecting numbers
            if user_input == "":
                if len(numbers) == 0:
                    print("Please enter at least one number!")
                    continue
                break
            
            # Convert input to float
            number = float(user_input)
            numbers.append(number)
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
    
    # Display collected numbers
    print(f"\nNumbers collected: {numbers}")
    
    # Show operation options
    print("\nSelect an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Average")
    
    # Get operation choice
    while True:
        operation = input("\nEnter operation (1-5): ").strip()
        if operation in ['1', '2', '3', '4', '5']:
            break
        print("Invalid choice! Please enter 1-5.")
    
    # Perform calculation
    result = None
    
    if operation == '1':  # Add
        result = sum(numbers)
        print(f"\nSum: {result}")
    
    elif operation == '2':  # Subtract
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        print(f"\nSubtraction result: {result}")
    
    elif operation == '3':  # Multiply
        result = 1
        for num in numbers:
            result *= num
        print(f"\nProduct: {result}")
    
    elif operation == '4':  # Divide
        result = numbers[0]
        try:
            for num in numbers[1:]:
                if num == 0:
                    print("\nError: Cannot divide by zero!")
                    return
                result /= num
            print(f"\nDivision result: {result}")
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero!")
            return
    
    elif operation == '5':  # Average
        result = sum(numbers) / len(numbers)
        print(f"\nAverage: {result}")
    
    print("\nCalculation complete!")


# Run the calculator
if __name__ == "__main__":
    simple_calculator()
