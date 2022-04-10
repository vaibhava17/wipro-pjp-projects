counter = 1
n = 10

while counter < n+1:
    if counter % 10 == 0:
        print(counter)
    else:
        print(counter, end=" ")
    counter += 1
