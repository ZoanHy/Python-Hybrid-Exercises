# FileNotFound
# with open("a_file.text") as file
# file.read()


# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Orange"]
# fruit = fruit_list[2]

# TypeError
# text = "abc"
# print(text + 5)

# Demo try catch else finally
# try:
#     file = open("abc.txt")
#     print("abc 2")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["abcc"])
# except FileNotFoundError:
#     print("There was an error")
#     file = open("abc.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     print("No error")
#     # content = file.read()
#     # print(content)
# finally:
#     raise TypeError("This is an error that I made up")
#     file.close()
#     print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
