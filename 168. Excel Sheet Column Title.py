class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        # radix = []
        while n > 26:
            if n % 26 == 0:
                # radix.append(26)
                res =  chr(26 + 64) + res
                n = n // 26 -1
            else:
                # radix.append(n%26)
                res = res + chr(n % 26 + 64)
                n = n//26
        res = chr(n + 64) + res

        #
        # radix.append(n)
        # for i in reversed(radix):
        #     res = res+chr(i + 64)
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(52))