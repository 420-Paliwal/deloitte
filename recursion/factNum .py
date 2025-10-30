def pName(n):
    if n == 1:
        return 1
    if (n <= 0):
        return 0
    else:
        return n * pName(n-1)

summ = pName()
print(summ)