def pName(name, n):
    if (n <= 0):
        return 
    else:
        print(name , n, end= " ")
        print()
        pName(name, n-1)
        

pName("John", 5)