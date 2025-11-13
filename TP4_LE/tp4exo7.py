binome = ("login1", "login2")
print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}.")

try:
    binome[1] = input("Nouveau login du binôme : ")
except TypeError:
    print("Impossible de modifier un élément d’un tuple (immutabilité).")

try:
    del binome[1]
except TypeError:
    print("Impossible de supprimer un élément d’un tuple.")

trinome = binome + ("login3",)
print("Nouveau tuple (trinôme) :", trinome)
print("→ Les tuples sont immuables, mais on peut en créer de nouveaux à partir d’anciens.")