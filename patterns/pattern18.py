def pattern1(n):
    for i in range(n):
        count = 65 + n - 1
        for j in range(i, -1, -1):
            print(chr(count - j), end=" ")
        print()
pattern1(5) 