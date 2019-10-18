from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None: return []
        if len(nums) == 1: return [nums]
        res = []
        for x in nums:
            ys = nums + []
            ys.remove(x)
            for y in self.permute(ys):
                if [x] + y not in res:
                    res.append([x] + y)
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [1,2,3]
    print(so.permute(nums))