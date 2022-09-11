
# Open, read & write File

# with open("my_text.txt") as file:
#
#     content = file.read()
#
#     print(content)
#
#     # file.close()

# with open("new_text11.txt", mode="a") as  file:
#     file.write("\nShibaaa")


# Absolute, Relative path

with open('C:/Users/ASUS/Downloads/new_text.txt') as file:
    print(file.read())

with open('..\\..\\..\\..\\..\\Downloads\\new_text.txt') as file:
    print(file.read())


