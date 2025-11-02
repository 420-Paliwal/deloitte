def dichash(arr,x):
    n = len(arr)
    hashh = {}
    for i in range(n):
        if arr[i] in hashh:
            hashh[arr[i]] += 1
        else:
            hashh[arr[i]] = 1
    return hashh.get(x, 0)

summ = dichash([1, 2, 3, 2, 1, 4, 2], 2)
print(summ)