class Solution:
    def intToRoman(self, num):

        m = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]

        d = [1000, 100, 10, 1]

        r = ''

        for k, v in enumerate(d):  #输出为带index 0 1000 ，1 100， 2 10， 3 1
            # print(k,v)
            r += m[k][int(num/v)]
            num = num % v

        return r

if __name__ == '__main__':
    so = Solution()
    num = 1994
    print(so.intToRoman(num))