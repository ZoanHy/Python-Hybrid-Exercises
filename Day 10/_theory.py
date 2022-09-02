import os
os.system("cls")

# Function with Outputs
def my_function():
    return 3 * 2

def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
    
    return f"{f_name.title()} {l_name.title()}"
    
print(format_name("Zoan", "Hy"))

def format_nameV2(f_name, l_name):
    """Check doc string and decribe it"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"{f_name.title()} {l_name.title()}"
    
print(format_nameV2(input("What's your first name? "), input("What's your last name? ")))
    