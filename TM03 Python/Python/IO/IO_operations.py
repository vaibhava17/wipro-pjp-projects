# Task 1
f = open("Iotext.txt", "r")
print(f.read())
f.close()


# Task 2
n = int(input("Enter a number of line you want to read : "))
f = open("Iotext.txt", "r")
for i in range(n):
    print(f.readline())
f.close()

# Task 3
f = open("Iotext.txt", "a+")
f.write("\nThis is a new line")
f.close()

# Task 4
f = open("Iotext.txt", "r")
line = f.read().split("\n")
print(line)
f.close()

# Task 5
f = open("Iotext.txt", "r")
longest_word = ""
for line in f:
    for word in line.split():
        if len(word) > len(longest_word):
            longest_word = word
print(f"The longest word is : {longest_word}")
f.close()

# Task 6
f = open("Iotext.txt", "r")
word_freq = {}
for line in f:
    for word in line.split():
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
print(word_freq)
f.close()