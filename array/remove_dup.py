class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        j = 0
        for i in range(1, n):
            if arr[i] != arr[j]:
                j += 1
                arr[j] = arr[i]
            arr[i] = None
        return j + 1
    
obj = Solution()
arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(obj.removeDuplicates(arr))
print(arr)