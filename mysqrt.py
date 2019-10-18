class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        min, max = 0,x
        mid = x//2
        while max>=min:
            if mid**2>x:
                max = mid-1
            elif mid**2<x:
                min = mid+1
            else:
                return mid
            mid=(max+min)//2

        return mid
        # min = 0
        # max = x
        # mid = x//2
        # while min<=max:
        #     m = mid*mid
        #     if m>x:
        #         max = mid-1
        #     elif m<x:
        #         min = mid+1
        #     else:
        #         return mid
        #     mid = (min+max)//2
        # return mid
so = Solution()
print(so.mySqrt(8))