row1 = ["⚪️","⚪️","⚪️"]
row2 = ["⚪️","⚪️","⚪️"]
row3 = ["⚪️","⚪️","⚪️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

y_position = int(position[1])
x_position = int(position[0])

map[y_position-1][x_position-1] = "🔴"

print(f"{row1}\n{row2}\n{row3}")

# print("\n")

# print(f"{map[0]}\n{map[1]}\n{map[2]}")

# map[0] = row1
# map[1] = row2
# map[2] = row3

# print("\n")

# print(f"{row1}\n{row1}\n{row1}")