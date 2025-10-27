def pattern1(n):
    for i in range(1, 2*n):
        star = i 
        if star > n:
            star = 2*n - star
        for j in range(star):
            print("*", end = " ")
        print()
pattern1(3)