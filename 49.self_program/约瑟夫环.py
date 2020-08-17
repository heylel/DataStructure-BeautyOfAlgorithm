# -*- coding:utf-8 -*-
# @File     :约瑟夫环
# @Author   :andy.zhong
# @Desc     :

class LinkNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class JosephCircle(object):
    def __init__(self,m):
        self.len=m
        self.head=LinkNode(0)
        cur=self.head
        for i in range(m):
            cur.next=LinkNode(i+1)
            cur=cur.next
            if i+1==m:
                cur.next=self.head.next
                break

    # 报m的删除，剩下r个人
    def baoshu(self,m,r):
        cur=self.head
        count=0
        while self.len>r:
            while count<m:
                cur=cur.next
                count+=1
                if count+1==m:
                    self.head=cur.next
                    cur.next=cur.next.next
                    self.len=self.len-1
                    print(f"本轮删除{self.head.val}\n还剩下{self.len}人,为{self.__str__()}")
                    count=0
                    cur=self.head
                    break
                continue



    def __str__(self):
        val=[]
        cur=self.head.next
        while cur :
            val.append(cur.val)
            cur=cur.next
            if cur.val==self.head.next.val:
                break
        return val


j=JosephCircle(30)
print(j.__str__())
j.baoshu(6,20)