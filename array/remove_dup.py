class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        count = 1 
        n = len(arr)
        j = 0
        for i in range(1, n):
            if arr[i] != arr[j]:
                count += 1
                j = i
        return count
    
obj = Solution()
print(obj.removeDuplicates([1, 1, 2, 2, 3, 4, 4, 5]))