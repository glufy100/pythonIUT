BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) convies a la fondue : "))

fromage_adapte = fromage * nbConvives / BASE
eau_adapte = eau * nbConvives / BASE
ail_adapte = ail * nbConvives / BASE
pain_adapte = pain * nbConvives / BASE

print("Pour faire une fondue fribourgeoise pour ", nbConvives, " personnes, il vous faut :")
print(fromage_adapte, " gr de fromage")
print(eau_adapte, " dl d'eau")
print(ail_adapte, " gousse(s) d'ail")
print(pain_adapte, " gr de pain")
