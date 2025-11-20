class Solution:
    def singleNumber(self, arr) -> int:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        for num, freq in count.items():
            if freq == 1:
                return num
            
obj = Solution()
arr = [4,1,2,1,2]
print(obj.singleNumber(arr))  # Output should be 4
