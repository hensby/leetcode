import sys
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sys.maxsize
        for i, num in enumerate(nums[:-2]):
            l, r = i+1, len(nums)-1
            while l < r:
                ans = num + nums[r] + nums[l]
                if abs(target - ans) < abs(target - res):
                    res = ans
                if ans == target: return res
                elif ans < target:  l+=1
                else:   r-=1
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [-1, 2, 1, -4]
    print(so.threeSumClosest(nums, 1))