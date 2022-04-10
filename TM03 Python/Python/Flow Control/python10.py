num = int(input("Enter number: "))
temp = num
rev = 0

while(num > 0):
    digit = num % 10
    rev = rev*10+digit
    num = num//10

if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
