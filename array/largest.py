class Solution:
    def largestElement(self, arr):
        maxx = arr[0]
        for i in arr:
            if i > maxx:
                maxx = i 
        return maxx
    
obj = Solution()
print(obj.largestElement([1, 2, 3, 0, -1, 99, 34])) 