class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # KMP算法
        i,j=0,0
        while i<len(haystack) and j<len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                i = i-j+1
                j = 0
        if j ==len(needle):
            return i-j
        else:
            return -1
so = Solution()
print(so.strStr("aaaaa","ll"))