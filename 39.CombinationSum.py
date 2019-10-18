from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates = sorted(candidates)
        self.combinationSumHelper(candidates, target, res, path, 0)
        return res

    def combinationSumHelper(self,candidates: List[int], target: int, res: List[List[int]], path: List, index):
        for i in range(index, len(candidates)):
            new = target-candidates[i]
            if new < 0:
                return
            else:
                if new == 0:
                    res.append(path + [candidates[i]])
                else:self.combinationSumHelper(candidates, new, res, path+[candidates[i]], i)


if __name__ == '__main__':
    so = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(so.combinationSum(candidates, target))