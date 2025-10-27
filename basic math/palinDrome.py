class Solution:
    def isPalindrome(self, n):
        rev = 0
        temp = n
        while(n):
            last = n%10
            n = n//10
            rev = (rev * 10) + last
        return temp == rev