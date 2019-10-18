class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:return True
        dict = {}
        return self.isHappyHelper(dict, n)


    def isHappyHelper(self, dict: {}, n: int, ):
        if n in dict.keys():return False
        if n == 1:return True
        res = 0
        for i in str(n):
            res+= int(i)**2
        dict[n] = res
        return self.isHappyHelper(dict, res)

if __name__ == '__main__':
    so = Solution()
    n = 7
    print(so.isHappy(n))
