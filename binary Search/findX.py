class Solution:
    def search(self, arr, x):
        n = len(arr)
        low = 0 
        high = n-1
        while(low <= high):
            mid = (low+high)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
obj = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
print(obj.search(arr, x))  # Output should be 4