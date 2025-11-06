import time

n = int(input("Entrez un nombre : "))

print("\nVersion FOR")
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)
print("Décollage !")

print("\nVersion WHILE")
i = n
while i >= 0:
    print(i)
    time.sleep(1)
    i -= 1
print("Décollage !")

