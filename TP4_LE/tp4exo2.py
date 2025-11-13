nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
notes = []
somme = 0

for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:
        print("Erreur : la note doit être comprise entre 0 et 20.")
        note = float(input(f"Note etudiant {i} : "))
    notes.append(note)
    somme += note

moyenne = somme / nombreEtudiants
print(f"\nMoyenne de classe : {round(moyenne, 2)}")

print("\nNuméro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = round(notes[i] - moyenne, 2)
    print(f"{i} | {notes[i]} | {ecart:+}")