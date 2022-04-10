# Task1
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"{a}/{b} = {div(a,b)}")
except ValueError:
    print("Error: Invalid input")

# Task2
def prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

try : 
    x = int(input("Enter a number: "))
    print(f"{x} is prime number: {prime_number(x)}")
except ValueError:
    print("Please enter a number")

# Task3
fileName = input("Enter a file name: ")
try:
    file = open(fileName)
    print(file.read().title())
    file.close()
except FileNotFoundError:
    print("File not found")

# Task 4
MyList = [1,2,3,4,5,6,7,8,9,10]
print(f"List is {MyList}")
try:
    index = int(input("Enter a index: "))
    print(f"Value present at {index} is {MyList[index]}")
except IndexError:
    print("Index out of range")