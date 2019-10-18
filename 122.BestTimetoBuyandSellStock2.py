class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices)==0:return 0
        maxprofit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                maxprofit=maxprofit+prices[i+1]-prices[i]
        return maxprofit


if __name__ == '__main__':
    so = Solution()
    # prices = [7,1,5,3,6,4]
    prices = [1,2,3,4,5]
    print(so.maxProfit(prices))