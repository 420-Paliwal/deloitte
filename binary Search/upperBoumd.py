class Solution:
    def upperBound(self, arr, x):
        n = len(arr)
        low = 0 
        high = n-1
        ub = n
        while(low <= high):
            mid = (low + high)//2
            if arr[mid] > x:
                ub = mid
                high = mid - 1
            elif arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return ub
    
obj = Solution()
arr = [1, 2,2,3]
x = 2
print(obj.upperBound(arr, x))  # Output should be 4