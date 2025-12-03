class Solution:
    def leaders(self, arr):
        n = len(arr)
        maxx = arr[n-1]
        temp = []
        for i in range(n-1,-1,-1):
            if arr[i] >= maxx:
                temp.append(arr[i])
            if arr[i] > maxx:
                maxx = arr[i]
        temp.reverse()
        return temp
    
obj = Solution()
arr = [16,17,4,3,5,2]
print(obj.leaders(arr))  # Output should be [17, 5, 2]
