# Task 1
MyList1 = [10, 20, 10, 40, 50]
print(
    f"MyList1 contains : {MyList1}\nMyList1 third element is :{MyList1[2]}\nMyList1 fifth element is : {MyList1[4]}")


# Task 2
MyList1.append(60)
print(
    f"MyList1 contains : {MyList1}\nMyList1 third element is :{MyList1[2]}\nMyList1 fifth element is : {MyList1[4]}")

# Task 3
MyList1 = MyList1[::-1]
print(
    f"MyList1 contains : {MyList1}\nMyList1 third element is :{MyList1[2]}\nMyList1 fifth element is : {MyList1[4]}")

# Task 4
print(f"{10} is appearing {MyList1.count(10)} times in MyList1")

# Task 5
MyList2 = [100, 200]
print(f"MyList2 contains : {MyList2}")

# Task 6
MyList2.insert(1, 150)
print(f"MyList2 contains : {MyList2}")

# Task 7
MyList1.pop(2)
print(f"MyList1 contains : {MyList1}")

# Task 8
MyList1.remove(10)
print(f"MyList1 contains : {MyList1}")
