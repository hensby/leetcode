class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     res = []
    #     weight = (len(s)/numRows*2-2)+1
    #
    #     for j in range(len(numRows)):
    #         if j == 0:
    #             for i in range(weight):
    #                 index = i*(numRows*2-2)
    #                 if index<=len(s):
    #                     res[i] = s[index]
    #         elif 0<j<numRows:


    def convert(self, s: str, numRows: int) -> str:
                """
                :type s: str
                :type numRows: int
                :rtype: str
                """
                if numRows == 1:
                    return s

                ans = ''
                interval = 2 * numRows - 2

                ans += s[::interval]  # 第0行,第一个例子里的0,4,8

                for i in range(1, numRows - 1):  # 第1到倒数第2行
                    innergap = interval - 2 * i
                    for j in range(i, len(s), interval):
                        ans += s[j]  # 例子里的1,5,9
                        if j + innergap < len(s):  # 注意越界
                            ans += s[j + innergap]  # 例子里的3,7

                ans += s[numRows - 1::interval]  # 最后1行,例子里的2,6
