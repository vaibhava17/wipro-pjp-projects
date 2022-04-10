import sys

numbers = sys.argv[1:11]

def prime_number(numbers) -> bool:
    for i in range(2, int(numbers)):
        if int(numbers) % i == 0:
            return False
    return True

print(f"Sum of the prime numbers in the numbers is : {sum(map(int, filter(prime_number, numbers)))}")
