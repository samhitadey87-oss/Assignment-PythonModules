import greetings

print(greetings.greet("Desmond"))
print(greetings.add(34, 76))

import calculate

# Get input from the user
num1 = float(input("Enter the first number:  "))
num2 = float(input("Enter the second number:  "))

# Display arithmetic operations
print("\n--- CALCULATOR RESULTS ---")

print("Addition:", calculate.addition(num1, num2))

print("Subtraction:", calculate.subtraction(num1, num2))
if num2 != 0:
    print("Division:", calculate.division(num1, num2))
    print("Floor Division:", calculate.floor_division(num1, num2))
    print("Modulus:", calculate.modulus(num1, num2))
else:
    print("Division: Cannot divide by zero")
    print("Floor Division: Cannot divide by zero")
    print("Modulus: Cannot divide by zero")

print("Multiplication:", calculate.multiplication(num1, num2))

print("Exponentiation:", calculate.exponentiation(num1, num2))