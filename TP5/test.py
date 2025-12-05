import os.path
import datetime

# Script de test 100% automatique pour TP5 (aucun input utilisateur)

# -------------------------------------------------
# Exercice 1 : nom et prénom (valeurs de test)
# -------------------------------------------------
print("--- Exercice 1 : nom et prénom ---")
nom1, prenom1 = "Durand", "alice"
nom2, prenom2 = "Martin", "bob"

pers1_aff = (prenom1.capitalize(), nom1.upper())
pers2_aff = (prenom2.capitalize(), nom2.upper())

pers1_tri = (nom1.lower(), prenom1.lower(), pers1_aff)
pers2_tri = (nom2.lower(), prenom2.lower(), pers2_aff)

personnes = [pers1_tri, pers2_tri]
personnes.sort(key=lambda p: (p[0], p[1]))

for _, _, (prenom, nom) in personnes:
    print(prenom, nom)

# -------------------------------------------------
# Exercice 2 : Notes (valeurs de test)
# -------------------------------------------------
print("\n--- Exercice 2 : Notes ---")
# (note, coeff)
notes_coeffs = [
    (12.0, 2),
    (9.5, 3),
    (14.0, 2),
    (11.0, 1),
    (8.0, 2),
]

notes = [n for n, _ in notes_coeffs]
coeffs = [c for _, c in notes_coeffs]

somme_pond = 0.0
somme_coeffs = 0
for n, c in notes_coeffs:
    somme_pond += n * c
    somme_coeffs += c

moyenne = somme_pond / somme_coeffs
admise = moyenne > 10 and all(n >= 8 for n in notes)

print(f"Moyenne générale (test) : {moyenne:.2f}")
print("Notes utilisées :", notes)
print("Coefficients :", coeffs)
if admise:
    print("L'étudiant est admis (test).")
else:
    print("L'étudiant n'est pas admis (test).")

# -------------------------------------------------
# Exercice 3 : Palindromes (plusieurs phrases de test)
# -------------------------------------------------
print("\n--- Exercice 3 : Palindromes ---")
phrases_test = [
    "Otto",
    "Esope reste ici et se repose",
    "Engage le jeu que je le gagne.",
    "Cours de Python",
]

for texte in phrases_test:
    nettoyee = ""
    for c in texte:
        if c.isalpha():
            nettoyee += c.lower()

    est_palindrome = True
    gauche = 0
    droite = len(nettoyee) - 1

    while gauche < droite and est_palindrome:
        if nettoyee[gauche] != nettoyee[droite]:
            est_palindrome = False
        gauche += 1
        droite -= 1

    if est_palindrome and len(nettoyee) > 0:
        resultat = "palindrome"
    else:
        resultat = "non palindrome"

    print(f"'{texte}' -> {resultat}")

# -------------------------------------------------
# Exercice 4 : La monnaie (plusieurs montants de test)
# -------------------------------------------------
print("\n--- Exercice 4 : La monnaie ---")

for somme in [0, 1, 2, 7, 627]:
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

# -------------------------------------------------
# Exercice 5 : Fiche de paye (plusieurs cas de test)
# -------------------------------------------------
print("\n--- Exercice 5 : Fiche de paye ---")
cas_heures = [
    (150, 10.0),   # seulement base
    (180, 10.0),   # base + 20h à 25%
    (220, 10.0),   # base + 40h à 25% + 20h à 50%
]

for heures, taux_horaire in cas_heures:
    salaire = 0.0

    if heures <= 160:
        salaire = heures * taux_horaire
    else:
        salaire = 160 * taux_horaire
        reste_h = heures - 160

        if reste_h <= 40:
            salaire += reste_h * taux_horaire * 1.25
        else:
            salaire += 40 * taux_horaire * 1.25
            reste_h -= 40
            salaire += reste_h * taux_horaire * 1.5

    print(f"Heures : {heures}, taux : {taux_horaire} € -> Salaire brut : {salaire:.2f} €")

# -------------------------------------------------
# Exercice 6 : Chaînes de caractères (tests sur les phrases 'wagon')
# -------------------------------------------------
print("\n--- Exercice 6 : Chaînes de caractères ---")

chaines_test = [
    "Le wagon bleu est rapide.",
    "Un petit wagon roule vite.",
    "Le ciel est bleu, comme un wagon.",
    "Wagon après wagon, le train avance.",
    "Il y a cinq wagons dans le train.",
    "La locomotive tire les wagons.",
    "Wagon, wagon, wagon, ciel bleu.",
    "Le train avance avec ses wagons.",
    "Un wagon rouge file à toute vitesse.",
    "Le wagon jaune transporte des marchandises.",
]

mot = "wagon"

taille_mot = 0
for _ in mot:
    taille_mot += 1

for chaine in chaines_test:
    print(f"\nChaîne de test : {chaine}")

    # 1. Taille de la chaîne (sans len)
    taille = 0
    for _ in chaine:
        taille += 1
    print("Taille de la chaîne :", taille)

    # 2. Pourcentage de voyelles
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

    # 3 et 4. Occurrences de 'wagon'
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

# -------------------------------------------------
# Exercice 7 : Dernière modification (tests sur des fichiers connus)
# -------------------------------------------------
print("\n--- Exercice 7 : Dernière modification ---")

# On utilise deux fichiers du répertoire TP5 pour le test
f1 = "TP5.pdf"
f2 = "nomprenom.py"

print(f"Fichiers testés : {f1} et {f2}")


def infos_fichier(nom):
    if os.path.isfile(nom):
        taille = os.path.getsize(nom)
        mtime = os.path.getmtime(nom)
        date = datetime.datetime.fromtimestamp(mtime)
        return True, taille, mtime, date
    else:
        return False, None, None, None

ex1, taille1, mtime1, date1 = infos_fichier(f1)
ex2, taille2, mtime2, date2 = infos_fichier(f2)

if not ex1:
    print(f"Le fichier {f1} n'existe pas.")
else:
    print(f"Fichier {f1} : taille {taille1} octets, dernière modification {date1}")

if not ex2:
    print(f"Le fichier {f2} n'existe pas.")
else:
    print(f"Fichier {f2} : taille {taille2} octets, dernière modification {date2}")

if ex1 and ex2:
    if mtime1 > mtime2:
        print(f"Le fichier le plus récent est {f1} ({date1}).")
    elif mtime2 > mtime1:
        print(f"Le fichier le plus récent est {f2} ({date2}).")
    else:
        print("Les deux fichiers ont la même date de modification.")
