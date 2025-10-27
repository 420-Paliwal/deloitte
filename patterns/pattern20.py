def pattern1(n):
    for i in range(1,2*n):
        star = i 
        if i > n:
            star = 2*n - i
        for j in range(star):
            print("*", end=" ")
        space  = 2*(n - i)
        if i > n:
            space = 2*(i - n)
        for s in range(space):
            print(" ", end=" ")
        star = i
        if star > n:
            star = 2*n - i
        for k in range(star):
            print("*", end=" ")
        print() 

pattern1(5) 