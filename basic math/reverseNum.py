class Solution:
    def reverseNumber(self, n):
        rev = 0
        while(n):
            last = n%10
            n = n//10
            rev = (rev * 10) + last
        return rev