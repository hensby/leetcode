class Solution:
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     if matrix == []:
    #         return False
    #     w = len(matrix[0])-1
    #     h = 0
    #
    #     while w >= 0 and h <= len(matrix)-1:
    #
    #         if matrix[h][w]==target:
    #             return True
    #         elif matrix[h][w]>target:
    #             w = w - 1
    #         elif matrix[h][w]<target:
    #             h = h + 1
    #     return False

    def searchMatrix2(self, matrix, target):
        """
                :type matrix: List[List[int]]
                :type target: int
                :rtype: bool
                """
        rs, re , cs, ce = 0, len(matrix)-1, 0, len(matrix[0])-1
        if matrix == []:return False
        return self.search(rs, re , cs, ce, matrix, target)


    def search(self,rs, re , cs, ce, matrix, target):
        if re < rs or ce < cs:return False
        r, c = (rs + re) // 2, (cs + ce) // 2
        if matrix[r][c]==target:return True
        elif matrix[r][c]> target:
            return self.search(rs, re, cs, c-1, matrix, target) or self.search(rs, r-1, c, ce, matrix, target)
        elif matrix[r][c]< target:
            return self.search(r+1, re, cs, c, matrix, target) or self.search(rs, re, c+1, ce, matrix, target)

if __name__ == '__main__':
    So = Solution()
    matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
    # matrix = [[-5]]
    print(matrix)
    print(So.searchMatrix2(matrix,5))