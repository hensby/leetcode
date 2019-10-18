class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in dic.keys():
                stack.append(i)
            elif i in dic.values():
                if len(stack)==0 or dic[stack[-1]]!=i:
                    return False
                else:
                    stack.pop()
        if len(stack)==0:
            return True
        else:
            return False

so = Solution()
s = "{[()]}"
print(so.isValid(s))



