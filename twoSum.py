class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range (len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return i,j
        #         else:
        #             continue


        n = len(nums)
        #创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            #字典d中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]],x
            #否则往字典增加键/值对
            else:
                d[a] = x
        #边往字典增加键/值对，边与nums[x]进行对比

so = Solution()
nums = [1,2, 6,7, 11, 15]
target = 9
print(so.twoSum(nums,target))
