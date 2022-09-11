list_1 = []
list_2 = []
with open("file1.txt") as file1:
    list_1 = [int(line.strip()) for line in file1.readlines()]

with open("file2.txt") as file2:
    list_2 = [int(line.strip()) for line in file2.readlines()]

result = [num for num in list_1 if num in list_2]

# Write your code above 👆

print(result)
