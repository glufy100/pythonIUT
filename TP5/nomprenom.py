nom1 = input("Entrez le nom de la première personne : ").strip()
prenom1 = input("Entrez le prénom de la première personne : ").strip()

nom2 = input("Entrez le nom de la deuxième personne : ").strip()
prenom2 = input("Entrez le prénom de la deuxième personne : ").strip()

pers1_aff = (prenom1.capitalize(), nom1.upper())
pers2_aff = (prenom2.capitalize(), nom2.upper())

pers1_tri = (nom1.lower(), prenom1.lower(), pers1_aff)
pers2_tri = (nom2.lower(), prenom2.lower(), pers2_aff)

personnes = [pers1_tri, pers2_tri]
personnes.sort(key=lambda p: (p[0], p[1]))

for _, _, (prenom, nom) in personnes:
    print(prenom, nom)
