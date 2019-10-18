class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i+=1
            else:
                break

        if i == len(nums):
            return len(nums)
        else:
            return i
so = Solution()
arr = [1,3,5,6]
print(so.searchInsert(arr,7))
