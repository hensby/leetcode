class Solution(object):
    def longestPalindrome(self, s):
        #KMP算法改进
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s)==1:
            return s


        result = ''
        maxlen = 0
        for i in range(len(s)):
            for x in range(maxlen,len(s)-i):
                tsr = s[i:i+x+1]
                rtsr = tsr[::-1]
                if tsr == rtsr and len(tsr)>maxlen:
                    maxlen = len(tsr)
                    result = tsr

        return result

if __name__ == '__main__':
    a = 'babad'
    solu = Solution()
    print(solu.longestPalindrome(a))