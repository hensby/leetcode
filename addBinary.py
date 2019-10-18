class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        intNum = int(a, 2) + int(b, 2)  # 2进制转换成10进制，再求和
        return bin(intNum)[2:]  # 10进制转换成2进制时前两位为0b，需要去除
so = Solution()
print(so.addBinary("11","101"))
    # 实例：
    #
    # 1.
    # x
    # 是数字的情况：
    #
    # 1
    # int(3.14)  # 3
    # 2
    # int(2e2)  # 200
    # 3
    # int(100, 2)  # 出错，base 被赋值后函数只接收字符串
    # 2.
    # x
    # 是字符串的情况：
    #
    # 1
    # int('23', 16)  # 35
    # 2
    # int('Pythontab', 8)  # 出错，Pythontab不是个8进制数
    # 3.
    # base
    # 可取值范围是
    # 2
    # ~36，囊括了所有的英文字母(不区分大小写)，十六进制中F表示15，那么G将在二十进制中表示16，依此类推....Z在三十六进制中表示35
    #
    # 1
    # int('FZ', 16)  # 出错，FZ不能用十六进制表示
    # 2
    # int('FZ', 36)  # 575
    # 4.
    # 字符串
    # 0
    # x
    # 可以出现在十六进制中，视作十六进制的符号，同理
    # 0
    # b
    # 可以出现在二进制中，除此之外视作数字
    # 0
    # 和字母
    # x
    #
    # int('0x10', 16)  # 16，0x是十六进制的符号
    # int('0x10', 17)  # 出错，'0x10'中的 x 被视作英文字母 x
    # int('0x10', 36)  # 42804，36进制包含字母 x