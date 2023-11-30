weight = int(input("How much do you weigh: "))
unit = input(' (L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilograms")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")
