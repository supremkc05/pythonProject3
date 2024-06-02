
# Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

    # Take input from the user

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice(1/2/3/4): ")


# Perform the selected operation
if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    result = num1 / num2
else:
    print("Invalid input")

# Print the result
print(f"Result: {result}")