class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        strList = []
        for i in pattern:
            strList.append(i)
        # print(words)
        # print(strList)
        if len(pattern) != len(words): return False
        return self.wordPatternHelper(strList,words) and self.wordPatternHelper(words,strList)


    def wordPatternHelper(self, pattern: list, words: list)-> bool:
        dict = {}
        for i in range(len(words)):
            if pattern[i] in dict.keys():
                if dict[pattern[i]]!=words[i]:return False
            dict[pattern[i]] = words[i]
        return True


if __name__ == '__main__':
    so = Solution()
    pattern = "abba"
    n = "dog cat cat fish"
    print(so.wordPattern(pattern,n))
