class Solution:
    def longestConsecutive(self, arr):
        # arr.sort()
        # n = len(arr)
        # count = 1
        # lgs = 1
        # for i in range(1,n):
        #     if arr[i] == arr[i-1] + 1:
        #         count += 1
        #     elif arr[i] == arr[i-1]:
        #         continue
        #     else:
        #         count = 1
        #     if count > lgs:
        #         lgs = count
        # return lgs   
        arr = set(arr)
        lg = 1
        for i in arr:
            if i-1 in arr:
                continue
            else:
                count = 1
                temp = i+1
                while(temp in arr):   
                    count+=1
                    temp+=1
                if count > lg:
                    lg = count
        return lg 

obj = Solution()
arr = [100, 4, 200, 1, 3, 2]
print(obj.longestConsecutive(arr))  # Output should be 4