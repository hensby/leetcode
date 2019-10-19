import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = re.sub(r'[^\w\s]','',s)
        print(s)
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    so = Solution()
    print(so.isPalindrome("A man, a plan, a canal: Panama"))