def pName( n):
    if (n <= 0):
        return 
    else:
        pName(n-1)
        print(n, end= " ")
        print()
        

pName(5)