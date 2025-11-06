moyenne = 0
i =0

while True:
    user_input = float(input("Entrez une note entre 0 et 20 (ou '-1' pour quitter) : "))
    i += 1
    if user_input == -1:
        break
    elif 0 <= user_input <= 20:
        moyenne += user_input
    else:
        print("Note invalide. Veuillez réessayer.")

if moyenne > 0:
    moyenne /= (i - 1)
    print("La moyenne des notes est :", moyenne)
else:
    print("Aucune note valide n'a été saisie.")