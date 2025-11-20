class Solution:
    def findMaxConsecutiveOnes(self, arr) -> int:
        count = 0 
        maxx = 0
        for i in arr:
            if i == 1:
                count += 1
                if count > maxx:
                    maxx = count
            else:
                count = 0 
        return maxx
    
obj = Solution()
arr = [1,1,0,1,1,1]
print(obj.findMaxConsecutiveOnes(arr))  # Output should be 3
