print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print("Result:", result)
        elif choice == '2':
            result = num1 - num2
            print("Result:", result)
        elif choice == '3':
            result = num1 * num2
            print("Result:", result)
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                result = num1 / num2
                print("Result:", result)
    else:
        print( "this is the Invalid Input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
