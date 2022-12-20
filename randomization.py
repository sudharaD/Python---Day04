import random
import module_example

random_number = random.randint(1, 4)

print(random_number)
print(module_example.pi)

random_float = random.random()

print(random_float)

print(random_number + random_float)
print(random_float * 5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}%")