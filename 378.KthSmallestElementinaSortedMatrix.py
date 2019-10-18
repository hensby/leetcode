from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left <= right:
            mid = (left + right) // 2
            loc = self.countLower(matrix, mid)
            print(left, right, mid)
            if loc >= k:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def countLower(self, matrix: List[List[int]], num: int)-> int:
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt

if __name__ == '__main__':
    so = Solution()
    matrix = [[1,2],[1,3]]
    k = 3
    print(so.kthSmallest(matrix, k))