from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:return [-1,-1]
        start, end = 0,len(nums)-1
        for i in range(len(nums)):
            # print(i)
            if target == nums[i]:
                start=i
                break
        while end > start:
            if target == nums[end]:
                break
            end-=1
        return [start, end]

if __name__ == '__main__':
    so = Solution()
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    nums = [1, 2]
    target = 2
    print(so.searchRange(nums, target))