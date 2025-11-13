date = input("Entrez une date (jjmmaaaa) : ")

if len(date) != 8 or not date.isdigit():
    print("Format incorrect. Utilisez jjmmaaaa.")
else:
    j = int(date[:2])
    m = int(date[2:4])
    a = int(date[4:])

    bissextile = (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

    if m < 1 or m > 12:
        print("Date incorrecte : mois invalide.")
    else:
        jours_mois = [31, 29 if bissextile else 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]
        if j < 1 or j > jours_mois[m - 1]:
            print("Date incorrecte : jour invalide.")
        else:
            print("Date correcte ✅")