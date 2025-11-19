class Solution:
    def check(self, arr: List[int]) -> bool:
        n = len(arr)
        count = 0 
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                count +=1 
            if count >= 2:
                return False
        if arr[n-1] > arr[0]:
            count += 1
        return count <= 1
    
obj = Solution()
print(obj.check([3,4,5,1,2]))