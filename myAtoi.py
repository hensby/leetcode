class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        numset = {'1','2','3','4','5','6','7','8','9','0'}
        op = {'+','-'}
        ms = str.lstrip()
        if ms=="" or ms.isspace():
            return 0
        low = 0
        res = 0
        while low < len(res) and res[low] in op:  # 判断符号位是否正确
            low += 1
        if low > 1 or low == len(ms): return 0  #只有符号没有数字，或者符号多于一个

        while low < len(ms):
            if ms[low] in numset:
                res = res * 10 + int(ms[low])
            else:
                break
            low += 1

        if ms[0] == "-":
            return max(-res, -0x80000000)
        return min(res, 0x7FFFFFFF)