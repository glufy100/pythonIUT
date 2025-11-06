import random

nombre_mystere = random.randint(0, 100)
compteur = 0
trouve = False

print("Devinez le nombre entre 0 et 100")

while not trouve:
    proposition = int(input("Votre proposition : "))
    compteur += 1

    if proposition < nombre_mystere:
        print("Plus grand")
    elif proposition > nombre_mystere:
        print("Plus petit")
    else:
        trouve = True
        print("Bravo ! Trouvé en", compteur, "essais")

