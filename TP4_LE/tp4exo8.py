etudiant1 = {
    "name": "Toto",
    "firstname": "Titi",
    "promo": 2024,
    "group": 202
}

print(f"Votre nom est '{etudiant1['name']}', prénom est '{etudiant1['firstname']}', "
      f"vous faites partie de la promo '{etudiant1['promo']}' et votre groupe est '{etudiant1['group']}'.")

print("\nLes clés du dictionnaire sont :")
for k in etudiant1.keys():
    print("-", k)

print("\nLes valeurs du dictionnaire sont :")
for v in etudiant1.values():
    print("-", v)

print("\nLes tuplets du dictionnaire sont :")
for item in etudiant1.items():
    print("-", item)

etudiant2 = {
    "name": "Tata",
    "firstname": "Tutu",
    "promo": 2024,
    "group": 102
}

binome = {"Etu1": etudiant1, "Etu2": etudiant2}

print("\nLes étudiants formant le binôme sont :")
for id, info in binome.items():
    print(f"- L'étudiant {info['name']} {info['firstname']} du groupe {info['group']}")