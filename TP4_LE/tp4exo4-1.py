L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
max_freq = 0
most_frequent = L1[0]

for i in range(len(L1)):
    freq = 0
    for j in range(len(L1)):
        if L1[i] == L1[j]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        most_frequent = L1[i]

print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({max_freq} x)")