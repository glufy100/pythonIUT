inf_10 = 0
entre_10_15 = 0
sup_15 = 0

for i in range(10):
    valeur = -1
    while valeur < 0 or valeur > 20:
        valeur = float(input("Entrez une valeur entre 0 et 20 : "))

    if valeur < 10:
        inf_10 += 1
    elif valeur < 15:
        entre_10_15 += 1
    else:
        sup_15 += 1

print("Inférieur à 10 :", inf_10)
print("Entre 10 et 15 :", entre_10_15)
print("Supérieur ou égal à 15 :", sup_15)

