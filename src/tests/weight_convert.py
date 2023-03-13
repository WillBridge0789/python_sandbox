weight_measure = str(input("(k) for Kilograms or (l) for pounds? "))
weight = int(input("Weight? "))
if weight_measure == "k":
    print(weight * 0.45359237)
else:
    print(weight)