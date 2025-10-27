def pattern1(n):
    for i in range(1,n+1):
        count = 65
        for space in range(n-i):
            print(" ", end=" ")
        for j in range(1,i*2):
            print(chr(count), end=" ")
            if j < i:
                count += 1
            else:
                count -= 1
        print()
pattern1(5) 