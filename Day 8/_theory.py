import os
os.system("cls")

# def greet():
#     print("hello Angela")
#     print("How do you do? ZoanHy")
#     print("I'm fine. Thanks")

# greet()

#_Parameter is the name of data
#_Argument is actually data
#Ex: name is parameter, "Angela" is argument
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print("How do you do? ZoanHy")
    
# greet_with_name("Angela")
# Positional Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
# greet_with("ZoanHy", "Da Nang")
greet_with("Da Nang", "ZoanHy")
greet_with(name="Angela", location="US")
# Keyword Arguments
def greet_with_keyword_arguments(name = "ZoanHy", location = "Da Nang"):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with_keyword_arguments()

    