# Paint Calculator
# I need to paint multipe walls, i need a tool to easily calculate how much paint to buy
# Each can of paint covers 5^2 metres

wallsize = input("Enter the size of your walls in square metres: ")

def paint_calculator(wallsize):
    # Each can of paint covers 5 square metres
    cansneeded = int(wallsize) / 5
    return cansneeded

print(f"Your will need to buy {print_calculator(wallsize)} cans of paint")