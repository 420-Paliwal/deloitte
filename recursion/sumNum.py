def pName(n):
    if (n <= 0):
        return 0
    else:
        return n + pName(n-1)

summ = pName(3)
print(summ)