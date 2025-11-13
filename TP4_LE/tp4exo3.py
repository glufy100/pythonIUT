nMax = 10
v1, v2 = [], []

n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
while n < 1 or n > nMax:
    n = int(input(f"Valeur incorrecte. Entrez une valeur entre 1 et {nMax} : "))

print("\nSaisie du premier vecteur :")
for i in range(n):
    v1.append(float(input(f"v1[{i}] = ")))

print("\nSaisie du second vecteur :")
for i in range(n):
    v2.append(float(input(f"v2[{i}] = ")))

produit = 0
for i in range(n):
    produit += v1[i] * v2[i]

print(f"\nLe produit scalaire de v1 par v2 vaut {produit}")