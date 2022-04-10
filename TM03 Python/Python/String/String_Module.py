# Task 1
MyString1 = "My Name is Vaibhav Agarwal."
print(f"Upper case letters = {sum(True for i in MyString1 if i.isupper())}")
print(f"Lower case letters = {sum(True for i in MyString1 if i.islower())}\n")

# Task 2
MyString2 = "level"
if MyString2 == MyString2[::-1]:
    print(f"String : ({MyString2}) is palindrome\n")
else:
    print(f"String : {MyString2} is not palindrome\n")

# Task 3
inputString = input("Enter a string : ")
print(f"Changed String : {inputString[:2] * len(inputString)}\n")

# Task 4
inputString = input("Enter a string : ")
if inputString[0] == 'x':
    print(f"Changed String : {inputString[1:]}\n")
elif inputString[-1] == 'x':
    print(f"Changed String : {inputString[:-1]}\n")
else:
    print(f"Changed String : {inputString}\n")

# Task 5
inputString = input("Enter a string : ")
inputNum = int(input("Enter a number : "))
print(f"Changed String : {inputString[-inputNum:] * inputNum}\n")
