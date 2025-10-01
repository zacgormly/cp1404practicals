"""Files"""

# 1

FILENAME = "names.txt"

name = input("Name: ")
out_file = open(FILENAME, 'w')
print(name, file=out_file)
out_file.close()

# 2

FILENAME = "names.txt"

in_file = open(FILENAME)
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3

FILENAME = "numbers.txt"

with open(FILENAME) as in_file:
    result = 0
    for i in range(2):
        number = int(in_file.readline())
        result += number
print(result)

# 4

FILENAME = "numbers.txt"

result = 0
with open(FILENAME) as in_file:
    for line in in_file:
        number = int(line)
        result += number
print(result)