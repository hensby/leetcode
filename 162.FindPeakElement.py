from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        r, l= len(nums)-1, 0
        while r>l:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1] or mid == 0 and nums[mid] > nums[mid+1] or mid == len(nums) - 1 and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid]>nums[mid+1]: r = mid
            else: l = mid+1
        return l

if __name__ == '__main__':
    so = Solution()
    # nums = [1,2,1,3,5,6,4]
    # nums = [1,2,3,1]
    nums = [5,6,7,8,9]
    print(so.findPeakElement(nums))
