class Solution:
    def majorityElement(self, arr) -> int:
        cnt = 0 
        n = len(arr)
        elem = None
        for i in range(n):
            if cnt == 0:
                cnt = 1
                elem = arr[i]
            elif arr[i] == elem:
                cnt += 1
            else:
                cnt -= 1
        cnt1 = 0
        for i in range(n):
            if elem == arr[i]:
                cnt1 += 1
        if cnt1 > n//2:
            return elem 
        else:
            return -1
        
obj = Solution()
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(obj.majorityElement(arr))  # Output should be 4
