import random

print("Welcom to Head or Tail!!!")

result = random.randint(1, 2)
coin = ""

if result == 1:
    coin = "Head"
else:
    coin = "Tail"

print(f"You got, {coin}")