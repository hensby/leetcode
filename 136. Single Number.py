from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i            #异或（xor）0⊕0=0，1⊕0=1，0⊕1=1，1⊕1=0（同为0，异为1）
        return ans

    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber2(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]




if __name__ == '__main__':
    so = Solution()
    nums = [4,1,2,1,2]
    print(so.singleNumber(nums))
    print(so.singleNumber1(nums))
    print(so.singleNumber2(nums))