from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        res = {}
        for i in range(len(s) - 9):
            tmp = s[i:i + 10]
            res[tmp] = res.get(tmp, 0) + 1
        return list([i for i in res.keys() if res[i] >= 2])

if __name__ == '__main__':
    so = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(so.findRepeatedDnaSequences(s))