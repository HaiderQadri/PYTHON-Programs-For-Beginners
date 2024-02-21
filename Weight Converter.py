weight = int(input("Enter you weight: "))
unit = input("(L)bs or (K)g ")
if unit.upper() == "L":
    converted_weight = weight * 0.45
    print(f"Yor are {converted_weight} Kgs")
else:
    converted_weight = weight / 0.45
    print(f"You are {converted_weight} Lbs")