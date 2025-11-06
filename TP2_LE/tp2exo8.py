x = float(input("Entrez un nombre decimal : "))

if ((x == 2 or not x < 2) and x < 3) or (not (x < 0 or x == 0) and (x < 1 or x == 1)) or ((x == -10 or not x < -10) and (x < -2 or x == -2)):
    print("x appartient a I")
else:
    print("x n'appartient pas a I")

