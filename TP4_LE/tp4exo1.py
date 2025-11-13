n = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
table = []

for i in range(10):
    table.append(round(n * i, 1))

for i in range(10):
    print(f"{n} * {i} = {table[i]}")