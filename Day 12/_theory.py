
#_ Namespaces Local vs Global Scope

"""Scope"""

# enemies = 1

# def increase_enemies():
#     enemies = 2
    
# increase_enemies()
# print(enemies)

"""Local scope"""

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()

"""Global Scope"""

# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)
    
# drink_potion()

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()
    
"""There is no Block Scope"""

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Ailen"]

# Create variable with function ==> Local Scope

# Create variable with block such as if, while, loop ==> not separate local scope

# if game_level < 5:
#     new_enemy = enemies[0]
    
"""Modifying Global Scope"""

enemies = 0

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")

"""Constants and Global Scope"""

PI = 3.14

PI = 1

print(PI)