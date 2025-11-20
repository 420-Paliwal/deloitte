class Solution:
    def moveZeroes(self, arr) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0 
        n = len(arr)
        for i in range(n):
            if arr[i] != 0:
                arr[j] = arr[i]
                j += 1
        for i in range(j,n):
            arr[i] = 0
        return 

obj = Solution()
arr = [0,1,0,3,12]  
obj.moveZeroes(arr)
print(arr)  # Output should be [1, 3, 12, 0, 0]