# Exercice 1 : Permutation de deux variables
x = int(input("Entrez x : "))
y = int(input("Entrez y : "))

print("\nAvant permutation:")
print("x :", x)
print("y :", y)

# Permutation avec variable temporaire
temp = x
x = y
y = temp

print("\nApres permutation:")
print("x :", x)
print("y :", y)
