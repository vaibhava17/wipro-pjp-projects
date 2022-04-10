# Task 1
def sum_list(array):
    sum = 0
    for i in array:
        sum += i
    return sum


array = [1, 2, 3, 4, 5]
print(f"Sum of array : {array} is : {sum_list(array)}\n")

# Task 2


def reverse_string(string):
    reverse_string = ""
    for i in string:
        reverse_string = i + reverse_string
    return reverse_string


string = "My Name is Vaibhav Agarwal"
print(f"Reverse of string : {string} is : {reverse_string(string)}\n")

# Task 3


def factorial(n):
    assert n >= 0, "n must be >= 0"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(f"Factorial of 5 is : {factorial(5)}\n")

# Task 4


def count_letters(string):
    upper_case = 0
    lower_case = 0
    for i in string:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
    return upper_case, lower_case


string = "My Name is Vaibhav Agarwal"
upper_case, lower_case = count_letters(string)
print(
    f"Count of upper case and lower case letters in string '{string}' is: \nUpper Case : {upper_case}\nLower Case : {lower_case}\n")


# Task 5
def print_even_numbers(array):
    for i in array:
        if i % 2 == 0:
            print(i, end=" ")


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Even numbers in array : {array} are : ", end="")
print_even_numbers(array)
print("\n")

# Task 6
# function to check if a number is prime or not


def is_prime(n):
    if n == 1:
        print(f"{n} is not a prime number")
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number")
    print(f"{n} is a prime number")


number = 23
is_prime(number)
