def insertionSort(arr, n):
    for i in range(1,n):
        temp = arr[i]
        j = i -1
        while(j >= 0 and temp < arr[j]):
            arr[j+1] = arr[j]
            j = j -1
        arr[j + 1] = temp
    return


arr = [64, 34, 25, 12, 22, 11, 90]
insertionSort(arr, len(arr))
print(arr)