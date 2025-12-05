notes = []
coeffs = []

for i in range(1, 6):
    ligne = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    morceaux = ligne.split()
    note = float(morceaux[0])
    coeff = int(morceaux[1])
    notes.append(note)
    coeffs.append(coeff)

somme_pond = 0.0
somme_coeffs = 0
for n, c in zip(notes, coeffs):
    somme_pond += n * c
    somme_coeffs += c

moyenne = somme_pond / somme_coeffs

admise = moyenne > 10 and all(n >= 8 for n in notes)

print("la moyenne est :", moyenne)
if admise:
    print("l'étudiant est admis")
else:
    print("l'étudiant n'est pas admis")
