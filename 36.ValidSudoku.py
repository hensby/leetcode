from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init data
        rows = [{}for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] !='.':
                    num = int(board[i][j])
                    box_index = (i // 3) * 3 + j // 3

                    rows[i][num] = rows[i].get(num,0)+1
                    columns[j][num] = columns[j].get(num,0)+1
                    boxes[box_index][num] = boxes[box_index].get(num,0)+1

                    if rows[i][num]>1 or columns[j][num]>1 or boxes[box_index][num]>1:return False
        return True

    def isValidSudoku1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x,y):
            tmp=board[x][y]; board[x][y]='D'
            for i in range(9):
                if board[i][y]==tmp: return False
            for i in range(9):
                if board[x][i]==tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[int(x/3)*3+i][int(y/3)*3+j]==tmp: return False
            board[x][y]=tmp
            return True

if __name__ == '__main__':
    so = Solution()
    p = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    p=[[".",".","4",".",".",".","6","3","."],
       [".",".",".",".",".",".",".",".","."],
       ["5",".",".",".",".",".",".","9","."],
       [".",".",".","5","6",".",".",".","."],
       ["4",".","3",".",".",".",".",".","1"],
       [".",".",".","7",".",".",".",".","."],
       [".",".",".","5",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."]]
    print(so.isValidSudoku(p))