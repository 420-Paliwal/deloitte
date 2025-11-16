class Solution:
    def secondLargestElement(self, arr):
        larg = arr[0]
        sec = -1
        for i in arr:
            if i > larg:
                if i > sec and i != larg:
                    sec = larg
                larg = i
            elif i > sec and i != larg:
                sec = i
        return sec        
    
obj = Solution()
print(obj.secondLargestElement([-1, 2, 3, 0, 1, 99, 34, 35]))