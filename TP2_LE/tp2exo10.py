somme_moyennes = 0
nb_eleves = 0

while True:
    nb_eleves += 1
    print(f"\n--- Élève {nb_eleves} ---")

    somme_notes = 0
    somme_coefs = 0
    nb_notes = 0

    while True:
        note = float(input("Entrez une note entre 0 et 20 (ou '-1' pour passer à l'élève suivant) : "))

        if note == -1:
            break
        elif 0 <= note <= 20:
            coef = float(input("Coefficient de cette note : "))
            somme_notes += note * coef
            somme_coefs += coef
            nb_notes += 1
        else:
            print("Note invalide. Veuillez réessayer.")

    if nb_notes > 0:
        moyenne_eleve = somme_notes / somme_coefs
        print(f"Moyenne de l'élève {nb_eleves} : {moyenne_eleve:.2f}")
        somme_moyennes += moyenne_eleve
    else:
        print("Aucune note valide pour cet élève.")
        nb_eleves -= 1

    continuer = input("\nAjouter un autre élève ? (oui/non) : ")
    if continuer.lower() != "oui":
        break

if nb_eleves > 0:
    moyenne_classe = somme_moyennes / nb_eleves
    print(f"\n=== Moyenne de la classe : {moyenne_classe:.2f} ===")
else:
    print("\nAucun élève n'a été saisi.")

