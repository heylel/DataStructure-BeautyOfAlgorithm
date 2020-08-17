class LinkNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class StringLinkList(object):
    def __init__(self,val:str):
        self.head=LinkNode(None)
        cur=self.head
        for ch in val:
            cur.next=LinkNode(ch,None)
            cur=cur.next
        self.head=self.head.next

    def is_palindrome(self):

        if not self.head.next:
            return True

        slow=self.head
        fast=self.head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp

        # 记录右侧链表起始位置，以便后续恢复
        newtmp=slow

        # 奇数,从奇数右侧一半链表开始比较
        if fast:
            slow=slow.next

        while slow:
            if slow.val!=prev.val:
                return False
            slow=slow.next
            pre_next=prev.next
            prev.next=newtmp
            newtmp=prev
            prev=pre_next

        return True


l=StringLinkList("asdfdsa")
print(l.is_palindrome())