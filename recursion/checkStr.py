def pName(arr):
    n = len(arr)    
    def reverseHelper(arr, start, end):
        if start >= end:
            return True
        elif arr[start] != arr[end]:
            return False
        else:
            return reverseHelper(arr, start + 1, end - 1)
    return reverseHelper(arr, 0, n - 1)

summ = pName("harsh")
print(summ)