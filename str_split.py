import random

name_string = input("Give me everybody's names, seperated by a comma. ")

names = name_string.split(", ")

print(names)

print(len(names))

random_name = random.randint(1, len(names))

print(random_name)

print(f"{names[random_name-1]} is going to buy the meal today!")