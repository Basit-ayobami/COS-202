def mc_calculator():
    result = 0
    print("="*40)
    print(" MATHEMATICAL CALCULATOR (MC) - COS202")
    print("="*40)
    print("Operators: + - * / \\ ^ %")
    print("Commands: C = Clear OFF = Exit")
    print("="*40)
    
    while True:
        print(f"\nCurrent Result: {result}")
        user_input = input("Enter operation: ").strip().upper()
        
        if user_input == "OFF":
            print("Calculator shutting down. Goodbye!")
            break
            
        elif user_input == "C":
            result = 0
            print("Result cleared to 0")
            continue
            
        try:
            # Format: operator number
            # Example: + 5 or * 3
            operator = user_input[0]
            number = float(user_input[1:].strip())
            
            if operator == '+':
                result += number
            elif operator == '-':
                result -= number
            elif operator == '*':
                result *= number
            elif operator == '/':
                if number == 0:
                    print("Error: Cannot divide by zero")
                    continue
                result /= number
            elif operator == '\\': # Integer division
                if number == 0:
                    print("Error: Cannot divide by zero")
                    continue
                result = result // number
            elif operator == '^': # Power
                result = result ** number
            elif operator == '%': # Modulus
                result = result % number
            else:
                print("Invalid operator. Use + - * / \\ ^ % C OFF")
                
        except (ValueError, IndexError):
            print("Invalid input. Format: + 5 or C or OFF")

if __name__ == "__main__":
    mc_calculator()