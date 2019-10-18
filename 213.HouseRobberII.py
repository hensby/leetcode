class Solution:
    def rob(self, nums) -> int:
        N = len(nums)
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        return max(self.robHelper(nums[1:N]), self.robHelper(nums[0:N-1]))

    def robHelper(self, nums):
        res = [0] * len(nums)
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            res[i] = max(res[i-2]+nums[i],res[i-1])
        return res[-1]

if __name__ == '__main__':
    so = Solution()
    # nums = [1,2,3,1]
    nums = [0,0]
    print(so.rob(nums))