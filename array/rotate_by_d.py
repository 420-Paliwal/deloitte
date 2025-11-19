class Solution:
    def rotate(self, arr, d):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        while (d >= 0):
            temp = arr[0]
            for i in range(n-1):
                arr[i] = arr[i+1]
            arr[n-1] = temp
            d -= 1
        return arr

obj = Solution()
print(obj.rotate([1, 2, 3, 4, 5], 2))