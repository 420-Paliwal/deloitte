class Solution:
    def longestSubarray(self, arr , k):
        n = len(arr)
        summ = 0 
        lenn = 0 
        j = 0 
        for i in range(n):
            summ += arr[i]
            while(j <= i and summ > k):
                summ -= arr[j]
                j += 1
            if summ == k:
                val = i+1 - j 
                if lenn < val:
                    lenn = val
        return lenn 
    
obj = Solution()
arr = [1, 1, 5, 2, 3]
k = 3
print(obj.longestSubarray(arr, k))  # Output should be 4