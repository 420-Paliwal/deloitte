class Solution:
    def isArmstrong(self, n):
        summ = 0
        temp = n
        while(n):
            last = n%10
            n = n//10
            summ += last*last*last
        return temp == summ