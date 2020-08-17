# -*- coding:utf-8 -*-
# @File     :328. 奇偶链表
# @Author   :andy.zhong
# @Desc     :

class LinkNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def oddEventList(self,head:LinkNode) -> LinkNode:
        if not head or not head.next:
            return head

        odd = head
        even=head.next
        prev2=even

        while even.next and even.next.next:
            odd.next=even.next
            even.next=even.next.next

            odd=odd.next
            even=even.next

        if even.next:
            odd.next=even.next
            even.next=None
            odd.next.next=prev2
        else:
            odd.next=prev2

        return head

