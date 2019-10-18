class Solution:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums)-1
        if len(nums)==1 :return nums[0]
        return self.binarySearch(l, r, nums)

    def binarySearch(self,l, r, nums):
        if l == r: return nums[l]
        mid = (l+r)//2
        if nums[mid] > nums[r]:
            return self.binarySearch(mid+1, r, nums)
        elif nums[mid] < nums[r]:
            return self.binarySearch(l, mid, nums)
        else:
            lmin = self.binarySearch(l, mid, nums)
            rmin = self.binarySearch(mid+1, r, nums)
            return (lmin if (lmin < rmin) else rmin)

if __name__ == '__main__':
    so = Solution()
    # nums = [2,2,2,0,-1]
    nums = [1,1,3]
    print(so.findMin(nums))