texte = input("Entrez un mot ou une phrase : ")

nettoyee = ""
for c in texte:
    if c.isalpha():
        nettoyee += c.lower()

est_palindrome = True
gauche = 0
droite = len(nettoyee) - 1

while gauche < droite and est_palindrome:
    if nettoyee[gauche] != nettoyee[droite]:
        est_palindrome = False
    gauche += 1
    droite -= 1

if est_palindrome and len(nettoyee) > 0:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")

