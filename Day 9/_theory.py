import os
os.system("cls")
# _Dictionaries
# key
programming_dictionary = {
    "Bug": "An error ...",
    123: "A piece of code ...",
    "Loop": "Doing something ..."
}

print(programming_dictionary[123])

# Adding new items to dictionary
programming_dictionary["ZoanHy"] = "Hello ZoanHy"
print(programming_dictionary)

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary

programming_dictionary["Bug"] = "Redefine Bug ..."
print(programming_dictionary)

# Loop throught a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paric", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting Dictionary in a List

travel_log_new = [
    {"country": "France", "cities_visited": [
        "Paric", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": [
        "Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
]
