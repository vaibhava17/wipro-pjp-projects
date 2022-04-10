# Task 1
Mydict1 = {0: 10, 1: 20}
Mydict1[2] = 30
print(f"Mydict1 = {Mydict1}\n")

# Task 2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated_dic = {**dic1, **dic2, **dic3}
print(f"Concatenated_dic = {concatenated_dic}\n")

# Task 3
if 2 in Mydict1:
    print("Key is present\n")
else:
    print("Key is not present\n")

# Task 4
for index, key in enumerate(Mydict1):
    print(f"Key no. {index + 1} of Mydict1 are : {key}")
    print(f"Value no. {index + 1} of Mydict1 are : {Mydict1[key]}")
    print(f"Keys and values of Mydict1 are : [{key} : {Mydict1[key]}]")

# Task 5
myDict2 = {i: i**2 for i in range(1, 16)}
print(f"myDict2 = {myDict2}\n")

# Task 6
sum_of_values = 0
for value in Mydict1.values():
    sum_of_values += value
print(f"Sum of values in Mydict1 = {sum_of_values}\n")
