class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 就是求2*5的个数,2个数总是多余5,所以是求5的个数
        # 先求5的倍数个数，再25,再125...
        res = 0
        while n:
            n = n // 5
            res += n
        return res

if __name__ == '__main__':
    so = Solution()
    n = 5
    print(so.trailingZeroes(n))
