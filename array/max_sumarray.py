class Solution:
    def maxSubArray(self, arr) -> int:
        n = len(arr)
        maxx = arr[0]
        summ = arr[0]
        for i in range(1,n):
            summ += arr[i]
            summ = arr[i] if summ < arr[i] else summ
            if maxx < summ:
                maxx = summ
        return maxx
    
obj = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(obj.maxSubArray(arr))  # Output should be 6