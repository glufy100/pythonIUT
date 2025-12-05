somme = int(input("Entrez une somme entière en euros : "))

reste = somme

nb100 = reste // 100
reste = reste % 100

nb50 = reste // 50
reste = reste % 50

nb10 = reste // 10
reste = reste % 10

nb2 = reste // 2
reste = reste % 2

nb1 = reste

print(f"{somme} euros, c'est donc {nb100} billets de 100, {nb50} de 50, {nb10} de 10, {nb2} pièces de 2 et {nb1} pièce 1.")

