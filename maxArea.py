class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height)-1
        while left<right:
            max_area = max(max_area,min(height[left],height[right])*(right-left))
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_area
so = Solution()
heitht = [1,8,6,2,5,4,8,3,7]
print(so.maxArea(heitht))

