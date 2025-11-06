X = float(input("Entrez X : "))
somme = 0
N = 0
while somme + N + 1 <= X:
    N += 1
    somme += N
print("N =", N)
print("Somme =", somme)
N = int(input("Entrez N : "))
somme = 0
for i in range(N + 1):
    somme += i
print("Somme =", somme)

