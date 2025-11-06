nombre = int(input("Entrez un nombre entier: "))

if nombre > 0:
    etat = "positif"
elif nombre < 0:
    etat = "negatif"
else:
    etat = "zero"

if nombre % 2 == 0:
    parite = "pair"
else:
    parite = "impair"

if nombre == 0:
    print("Le nombre est zero (et il est pair)")
else:
    print("Le nombre est ", etat, "et", parite)