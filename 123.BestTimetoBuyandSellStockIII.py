class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0: return 0
        maxpro = 0
        for i in range(len(prices)):
            maxpart = self.maxProfit2(prices[:i])+self.maxProfit2(prices[i:])
            maxpro = max(maxpro,maxpart)
        return maxpro


    def maxProfit2(self, prices) -> int:
        if len(prices) == 0: return 0
        min, maxprofit = prices[0], 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i] - min)
        return maxprofit


if __name__ == '__main__':
    so =Solution()
    prices = [3,3,5,0,0,3,1,4]
    print(so.maxProfit(prices))