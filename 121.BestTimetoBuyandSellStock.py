class Solution:
    def maxProfit(self, prices) -> int:
        min, maxprofit = prices[0], 0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            else:maxprofit=max(maxprofit, prices[i]-min)
        return maxprofit

if __name__ == '__main__':
    so = Solution()
    prices = [7,1,5,3,6,4]
    print(so.maxProfit(prices))