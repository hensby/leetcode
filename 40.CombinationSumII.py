from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates = sorted(candidates)
        self.combinationSunHelper(candidates, target, path, res)

        return res

    def combinationSunHelper(self, candidates: List[int], target: int, path: List[int], res: List[List[int]]):
        for i in range(len(candidates)):
            new = target - candidates[i]
            if new < 0: return
            else:
                if new == 0:
                    if path + [candidates[i]] in res:return
                    else:res.append(path + [candidates[i]])
                elif new > 0:
                    self.combinationSunHelper(candidates[i+1:], new, path+[candidates[i]], res)

if __name__ == '__main__':
    so = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = so.combinationSum2(candidates, target)
    print(res)
