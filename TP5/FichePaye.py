heures = float(input("Nombre d'heures travaillées : "))
taux_horaire = float(input("Salaire horaire : "))

salaire = 0.0

# Jusqu'à 160 h
if heures <= 160:
    salaire = heures * taux_horaire
else:
    salaire = 160 * taux_horaire
    reste = heures - 160

    # Entre 161 et 200 (maj +25%)
    if reste <= 40:
        salaire += reste * taux_horaire * 1.25
    else:
        salaire += 40 * taux_horaire * 1.25
        reste -= 40
        # Au-delà de 200 (maj +50%)
        salaire += reste * taux_horaire * 1.5

print(f"Salaire brut : {salaire:.2f} €")
