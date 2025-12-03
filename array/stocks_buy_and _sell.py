class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        mini = prices[0]
        profit = 0
        for i in prices:
            cost = i - mini
            profit = max(cost, profit)
            mini = min(i, mini)
        return profit 
    
obj = Solution()
prices = [7,1,5,3,6,4]
print(obj.maxProfit(prices))  # Output should be 5