class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits)==0:
            digits = [1]
        elif digits[-1]==9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1]+=1
        return digits
so = Solution()
print(so.plusOne([1,9,9,9,9,9]))