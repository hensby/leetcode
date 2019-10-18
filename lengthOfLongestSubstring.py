class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d_map = {}
        start = maxlength = 0
        for i in range(len(s)):
            if s[i] in d_map and start<= d_map[s[i]]:
                start = d_map[s[i]]+1
            else:
                maxlength = max(maxlength,i-start+1)
            d_map[s[i]] = i
        return maxlength

so = Solution()
str = 'abcabcbbabcdefg'
print(so.lengthOfLongestSubstring(str))