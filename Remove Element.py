class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i,j,size = 0,0,len(nums)
        while i < size:
            if nums[i] != val:
                nums[j] = nums[i]
                j +=1
            i+=1
        return j
so = Solution()
arr=[0,1,2,2,3,0,4,2]
print(so.removeElement(arr,2))
print(arr)