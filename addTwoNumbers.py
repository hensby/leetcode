# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:34:35 2018

@author: Saul
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        tmp =  ListNode(0)
        res = tmp
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next
            if l2:
                tmpsum = tmpsum+l2.val
                l2 = l2.next
            tmplast = (tmpsum+flag)%10
            flag = (tmpsum+flag)//10
            res.next = ListNode(tmplast)
            res = res.next
        if flag:
            res.next= ListNode(1)
        res= tmp.next
        del tmp
        return res