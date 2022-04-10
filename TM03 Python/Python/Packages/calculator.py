# Task 1
import math_module


def calculator():
    choice = 0
    while choice != 5:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            print("Addition of two numbers is : ", math_module.add(num1, num2))
        elif choice == 2:
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            print("Subtraction of two numbers is : ",
                  math_module.sub(num1, num2))
        elif choice == 3:
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            print("Multiplication of two numbers is : ",
                  math_module.mul(num1, num2))
        elif choice == 4:
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            print("Division of two numbers is : ", math_module.div(num1, num2))
        elif choice == 5:
            print("Thank you for using the calculator.")
        else:
            print("Invalid choice")


calculator()
