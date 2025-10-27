def pattern1(n):
    for i in range(1, n+1):
        value = 1
        if i % 2 == 0:
            value = 0
        for j in range(i):
            print(value, end = " ") 
            value = 1 - value
        print()
pattern1(5)