a = input("Entrez la premiere valeur : ")
b = input("Entrez la deuxieme valeur : ")
c = input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

temp = a
a = b
b = c
c = temp

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)