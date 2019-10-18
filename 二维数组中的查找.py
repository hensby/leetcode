class Solution1:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        ans = False
        for i in range (len(array)):
            if len(array[i]) == 0:
                return False
            if target in array[i]:
                ans = True
                break
        return  ans

# # -*- coding:utf-8 -*-
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         ans = False
#         for i in range (len(array)):
#             if target in array[i]:
#                 ans = True
#                 break
#         return ans
# while True:
#     try:
#         so = Solution()
#         list = list(eval(input()))
#         target = list[0]
#         array = list[1]
#         print(so.Find(target,array))
#     except:
#         break


so = Solution1()
print(so.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
print(so.Find(16,[[]]))


