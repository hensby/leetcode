class Solution:
    def countStr(self, s):
        count = 0;
        ans = "";
        tmp = s[0]
        for i in range(len(s)):
            if s[i] == tmp:
                count += 1
            else:
                ans += str(count) + tmp
                tmp = s[i];
                count = 1
        ans += str(count) + tmp
        return ans

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        while n > 1:
            ans = self.countStr(ans)
            n -= 1
        return ans


    def countAndSay1(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        n -= 1
        while n > 0:
            res = ""
            pre = ans[0]
            count = 1
            for i in range(1, len(ans)):
                if pre == ans[i]:
                    count += 1
                else:
                    res += str(count) + pre
                    pre = ans[i]
                    count = 1
            res += str(count) + pre
            ans = res
            n -= 1
        return ans

so = Solution()
for i in range(15):
    print(so.countAndSay(i))
for i in range(15):
    print(so.countAndSay1(i))