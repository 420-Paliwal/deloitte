def pattern1(n):
    for i in range(n):
        count = 65
        for j in range(i+1):
            print(chr(count), end=" ")
            count += 1
        print()
pattern1(5) 