from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a / b = 2.0, b / c = 3.0
        # 问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
        # 返回[6.0, 0.5, -1.0, 1.0, -1.0]
        # equations(方程式) = [["a", "b"], ["b", "c"]],
        # values(方程式结果) = [2.0, 3.0],
        # queries(问题方程式) = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]].
