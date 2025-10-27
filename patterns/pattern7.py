def pattern1(n):
    for i in range(1,n + 1):
        for space in range(n-i):
            print(" ", end = " ")
        for star in range(2*i-1):
            print("*", end = " ")
        print()


    # for i in range(n):
    #     for space in range(n-i-1):
    #         print(" ", end = " ")
    #     for star in range(2*i+1):
    #         print("*", end = " ")
    #     print()

pattern1(3)