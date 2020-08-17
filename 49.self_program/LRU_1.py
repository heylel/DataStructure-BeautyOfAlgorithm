# -*- coding:utf-8 -*-
# @File     :test
# @Author   :andy.zhong
# @Desc     :

import random
import time

class ListNode(object):
    def __init__(self,val,n=None):
        self.val=val
        self.next=n

class LRUCacheLink(object):
    def __init__(self,capacity:int=10):
        self.cap=capacity
        self.head=ListNode(None,None)
        self.length=0

    def insert_to_head(self,n):
        n.next=self.head.next
        self.head.next=n



    def get(self,val) ->  bool:
        cur=self.head
        # 用于记录尾节点的前一个节点,用于去除尾节点
        prev_2=cur
        while cur.next:
            if cur.next.val==val:
                tmp=cur.next
                cur.next=cur.next.next
                self.insert_to_head(tmp)
                return True
            prev_2=cur
            cur=cur.next

        # 不在LRU情况
        self.insert_to_head(ListNode(val))
        self.length+=1
        if self.length>self.cap:
            prev_2.next=None
        return False


    def __str__(self):
        LRU_DATA=[]
        cur=self.head
        while cur.next:
            LRU_DATA.append(str(cur.next.val))
            cur=cur.next
        return "->".join(LRU_DATA)




class LRUCacheArray(object):

    def __init__(self,capacity:int=10):
        self.cap=capacity
        self.data=[]

    def get(self,val) -> bool:
        for idx,el in enumerate(self.data):
            if el==val:
                self.data.insert(0,self.data.pop(idx))
                return True

        self.data.insert(0,val)
        if len(self.data)>self.cap:
            self.data.pop(-1)

        return False

    def __str__(self):
        return '->'.join([str(i) for i in self.data])

l=LRUCacheLink(30)
for i in range(30):
    #print(i)
    a=random.randint(30,60)
    print(f"search {a} , current LRU:{l.__str__()}")
    if l.get(a):
        print("cache 命中")
    else:
        print("未命中")

    time.sleep(1)