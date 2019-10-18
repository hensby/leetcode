class Solution:
    def findNthDigit(self, n):
        amount = 0
        for i in range(9):
            pin = amount
            amount = int(str(i) + (str(8) * i) + '9')
            if n < amount:
                sub = n - pin
                count_num = (sub // (i + 1)) + (10 ** i)
                lis = str(count_num - 1)[-1] + str(count_num)[:i + 1]
                return int(lis[sub % (i + 1)])

    def findNthDigit1(self, n: int) -> int:
        digital = 1
        while n > 9*digital*pow(10,digital-1):
            n -= 9*digital*pow(10,digital-1)
            digital+=1
        a = int((n-1)//digital)
        b = int((n-1)%digital)
        nums = 10**(digital-1)+a
        res = int(str(nums)[b])
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.findNthDigit1(33))