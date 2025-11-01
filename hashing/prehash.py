def preHash(arr, x):
    n = len(arr)
    hassh = [0]* n
    for i in range(n):
        hassh[arr[i]] += 1
    return hassh[x]

summ = preHash([1, 2, 3, 2, 1, 4, 2], 2)
print(summ)