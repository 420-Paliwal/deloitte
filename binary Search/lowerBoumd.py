class Solution:
    def lowerBound(self, arr, x):
        n = len(arr)
        low = 0 
        high = n-1
        lb = n
        while(low <= high):
            mid = (low + high)//2
            if arr[mid] >= x:
                lb = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return lb 
    
obj = Solution()
arr = [1, 2, 4, 4, 5, 6, 8, 9]
x = 4
print(obj.lowerBound(arr, x))  # Output should be 2