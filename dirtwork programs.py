number_of_blocks = int(input("Enter the total number of blocks:"))

height = (number_of_blocks / 4) + 11
height = height.__ceil__()
print(height)

help(round)
