
# Definition for a QuadTree node.
from typing import List
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(grid, a, b, N):
            sum = 0
            for i in range(N):
                for j in range(N):
                    sum += grid[a + i][b + j]
            if sum == 0 or sum == N * N:
                isLeaf = True
            else:
                isLeaf = False
            if isLeaf:
                root = Node(sum > 0, True, None, None, None, None)
                return root
            else:
                root = Node('*', False, None, None, None, None)
                N //= 2
                root.topLeft = dfs(grid, a, b, N)
                root.topRight = dfs(grid, a, b + N, N)
                root.bottomLeft = dfs(grid, a + N, b, N)
                root.bottomRight = dfs(grid, a + N, b + N, N)
                return root

        return dfs(grid, 0, 0, len(grid))

if __name__ == '__main__':
    so = Solution()
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    print(so.construct(grid))

