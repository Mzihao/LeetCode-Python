"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

link: https://leetcode-cn.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 考虑空值
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # 创建一个存储结果的Listnode
        result = ListNode(0)
        # p用于进位，result用于保留结果
        p = result

        # 创建一个保存进位的变量
        carry = 0

        # length相等部分
        while l1 and l2:
            # 相加超过10则取余
            p.next = ListNode((l1.val + l2.val + carry) % 10)

            # 取进位
            carry = (l1.val + l2.val + carry) // 10

            # 在Listnode中获取下一个节点
            l1 = l1.next
            l2 = l2.next

            # 存储Listnode的变量也要前进一位
            p = p.next

        # 考虑l1比l2长的情况
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next

        # 考虑l2比l1长的情况
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next

        if carry == 1:
            p.next = ListNode(1)

        # 初始化是第一个节点是0，所以要next
        return result.next
