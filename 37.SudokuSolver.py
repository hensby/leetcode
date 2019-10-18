from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x,y):
            # init data
            rows = [{} for i in range(9)]
            columns = [{} for i in range(9)]
            boxes = [{} for i in range(9)]

            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        num = int(board[i][j])
                        box_index = (i // 3) * 3 + j // 3

                        rows[i][num] = rows[i].get(num, 0) + 1
                        columns[j][num] = columns[j].get(num, 0) + 1
                        boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                        if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1: return False
            return True
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in '123456789':
                            board[i][j]=k
                            if isValid(i,j) and dfs(board):
                                return True
                            board[i][j]='.'
                        return False
            return True
        dfs(board)


if __name__ == '__main__':
    so = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    so.solveSudoku(board)
    print(board)