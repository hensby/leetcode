class Solution:
    def findMin(self, nums) -> int:
        l , r = 0 , len(nums)-1
        print(l,r,nums)
        return self.binarySearch(l,r,nums)

    def binarySearch(self, l , r , nums):
        if nums[l] > nums[r]:
            # print(l)
            l = l + 1
            return self.binarySearch(l,r,nums)
        elif nums[l] <= nums[r]:
            print(nums[l])
            return nums[l]

if __name__ == '__main__':
    so = Solution()
    # nums = [3,4,5,1,2]
    nums = [3,1]
    print(so.findMin(nums))