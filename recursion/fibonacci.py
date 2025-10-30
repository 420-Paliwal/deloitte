def pName(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    return pName(n-1) + pName(n-2)
summ = pName(10)
print(summ)