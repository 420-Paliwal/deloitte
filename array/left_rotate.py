class Solution:
    def rotateArrayByOne(self, arr):
        temp = arr[0]
        n = len(arr)
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = temp
        return arr
    
obj = Solution()
print(obj.rotateArrayByOne([1, 2, 3, 4, 5]))