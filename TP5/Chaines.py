chaine = input("Entrez une chaîne de caractères (max 100) : ")

taille = 0
for _ in chaine:
    taille += 1

print("Taille de la chaîne :", taille)

voyelles = "aeiouyAEIOUY"
nb_voyelles = 0
for c in chaine:
    if c in voyelles:
        nb_voyelles += 1

if taille > 0:
    pourcentage = nb_voyelles * 100.0 / taille
else:
    pourcentage = 0.0

print(f"Pourcentage de voyelles : {pourcentage:.2f}%")

mot = "wagon"

taille_mot = 0
for _ in mot:
    taille_mot += 1

premiere_pos = -1
nb_occurrences = 0

i = 0
while i <= taille - taille_mot:
    j = 0
    correspond = True
    while j < taille_mot and correspond:
        if chaine[i + j] != mot[j]:
            correspond = False
        j += 1

    if correspond:
        nb_occurrences += 1
        if premiere_pos == -1:
            premiere_pos = i
    i += 1

if premiere_pos != -1:
    print("'wagon' est une sous-chaîne, première occurrence à l'indice", premiere_pos)
else:
    print("'wagon' n'est pas une sous-chaîne de la chaîne donnée.")

print("Nombre d'occurrences de 'wagon' :", nb_occurrences)

