from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = set(nums1), set(nums2)
        print(a,b)
        return list(a & b)

if __name__ == '__main__':
    so = Solution()
    nums1, nums2 = [4,9,5], [9,4,9,8,4]
    print(so.intersection(nums1,nums2))
