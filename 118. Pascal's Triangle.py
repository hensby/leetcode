from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        res = [[1]]
        if numRows == 1: return res
        t = [1, 1]
        res.append(t)
        if numRows == 2: return res
        return self.generateHelper(3, numRows, t, res)

    def generateHelper(self, level, numRows: int, lastTmp: list, res: List[List[int]]):
        if level == numRows + 1: return res
        tmp = [1] * level

        for i in range(level-2):
            tmp[i + 1] = lastTmp[i] + lastTmp[i + 1]
        res.append(tmp)
        level += 1
        return self.generateHelper(level, numRows, tmp, res)


if __name__ == '__main__':
    so = Solution()
    print(so.generate(5))
