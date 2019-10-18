from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        dp = [0 for x in range(len(nums))]
        print(dp)
        index = [-1 for x in range(len(nums))]
        max_len, max_index = 0, -1
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    index[i] = j
                if dp[i] > max_len:
                    max_len = dp[i]
                    max_index = i
        arr = []
        while True:
            if max_index != -1:
                arr.append(nums[max_index])
                max_index = index[max_index]
            else:
                break
        return arr[::-1]

if __name__ == '__main__':
    so = Solution()
    nums = [1,2,3]
    print(so.largestDivisibleSubset(nums))