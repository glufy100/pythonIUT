jour = int(input("Entrez le jour du mois (1-31) : "))
heure = int(input("Entrez l'heure (0-23) : "))
minute = int(input("Entrez la minute (0-59) : "))

minutes_par_jour = 24 * 60
minutes_ecoulees = (jour - 1) * minutes_par_jour + heure * 60 + minute

print(f"Nombre de minutes écoulées depuis le début du mois : {minutes_ecoulees}")