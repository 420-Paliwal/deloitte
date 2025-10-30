def pName( n):
    if (n <= 0):
        return 
    else:
        print(n, end= " ")
        print()
        pName(n-1)
        

pName(5)