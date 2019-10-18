class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0: return 0
        res = [0x7FFFFFFF]*(n+1)
        res[0] = 0
        res[1] = 1
        for i in range(2,n+1):
            j = 1
            while j*j<=i:
                res[i] = min(res[i-j*j]+1, res[i])
                j = j+1
        return res[n]

if __name__ == '__main__':
    so = Solution()
    n = 8829
    print(so.numSquares(n))
