def pattern1(n):
    for i in range(n):
        for j in range(n-i-1,-1,-1):
            print("*", end= " ")
        for space in range(i*2):
            print(" ", end=" ")
        for K in range(n-i-1,-1,-1):
            print("*", end= " ")
        print()
    
    for i in range(n):
        for j in range(i+1):
            print("*", end= " ")
        for space in range((n-i-1)*2):
            print(" ", end=" ")
        for K in range(i+1):
            print("*", end= " ")
        print()

pattern1(5) 