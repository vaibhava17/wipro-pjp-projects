# Task 1
MyTuple1 = (10, 20, 30, 40, 50)
print(
    f"4th element from first and 4th element from last = {MyTuple1[3]}, {MyTuple1[-4]}")

# Task 2
if 10 in MyTuple1:
    print("Element is present\n")
else:
    print("Element is not present\n")

# Task 3
MyList1 = [50, 40, 30, 20, 10]
MyTuple2 = tuple(MyList1)
print(f"Tuple after conversion from list = {MyTuple2}\n")

# Task 4
print(f"Element on the third index is {MyTuple2[2]}")

# Task 5
MyList2 = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
MyList2[-1] = MyList2[-1][:-1] + (100,)
print(f"List after replacement = {MyList2}\n")
