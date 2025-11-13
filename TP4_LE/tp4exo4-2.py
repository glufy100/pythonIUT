L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
max_freq = 0
most_frequent = L1[0]

for n in L1:
    freq = L1.count(n)
    if freq > max_freq:
        max_freq = freq
        most_frequent = n

print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({max_freq} x)")