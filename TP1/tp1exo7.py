valeurs = [
    (5, 8, 2),
    (3, 3, 9),
    (5, 3, 7)
]

for (x1, x2, x3) in valeurs:
    print("\n----------------------------------")
    print("x1 =", x1, " x2 =", x2, " x3 =", x3)
    print("----------------------------------")

    # 1)
    condition = not(x1 == x2) and not(x1 == x2)
    if condition:
        print("1) not(x1 == x2) and not(x1 == x2) = VRAI")
    else:
        print("1) not(x1 == x2) and not(x1 == x2) = FAUX")

    # 2)
    condition = (x1 > x2) or (x3 < x1)
    if condition:
        print("2) (x1 > x2) or (x3 < x1) = VRAI")
    else:
        print("2) (x1 > x2) or (x3 < x1) = FAUX")

    # 3)
    condition = (x1 < x2) and (x2 < x3)
    if condition:
        print("3) (x1 < x2) and (x2 < x3) = VRAI")
    else:
        print("3) (x1 < x2) and (x2 < x3) = FAUX")

    # 4)
    condition = not((x1 > x2) and (x1 < x3))
    if condition:
        print("4) not((x1 > x2) and (x1 < x3)) = VRAI")
    else:
        print("4) not((x1 > x2) and (x1 < x3)) = FAUX")

    # 5)
    condition = (x1 == x2) or (x3 == x1) or (x2 == x3)
    if condition:
        print("5) (x1 == x2) or (x3 == x1) or (x2 == x3) = VRAI")
    else:
        print("5) (x1 == x2) or (x3 == x1) or (x2 == x3) = FAUX")
