def check(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            return False
    return True

checked = check([1, 2, 2, 3, 4])
print(checked)