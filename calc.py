def calaculator():
    print("Select operator: ")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3.Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4):")

    num1 =float(input("Enter first number:"))
    num2 =float(input("Enter second number:"))

    if choice == '1':
        print("Addition:", num1 + num2)
    elif choice == '2':
        print("Subtraction:", num1 - num2)
    elif choice == '3':
        print("Multiplication:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Division:", num1 / num2)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid choice")
    print("Do you want to continue? (yes/no)")
    continue_calc = input()
    if continue_calc.lower() != 'yes':
        print("Calculator closed.")
    else:
        calaculator()
