class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j,max=0,nums[1]
        while j<len(nums):
            res = 0
            i = j
            while i<len(nums):
                res = res+nums[i]
                if res >max:
                    max=res
                i+=1
            j+=1
        return max


    def maxSubArray1(self, nums):

        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])
            maxSum = max(maxSum, preSum)
        return maxSum
so = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(so.maxSubArray(arr))
print(so.maxSubArray1(arr))