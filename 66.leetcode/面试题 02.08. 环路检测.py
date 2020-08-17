# -*- coding:utf-8 -*-
# @File     :面试题 02.08. 环路检测
# @Author   :andy.zhong
# @Desc     :
'''
给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。

 
示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
 

示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
 

示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
 

进阶：
你是否可以不用额外空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
解题思路


如果链表中有环，那么快慢指针就一定可以相遇（且一定再环上，如图上的c点），此时快指针移动过的距离是慢指针的2倍，根据图中的参数，我们可以写出以下等式：

(m+y)*2=m+xn+y //这里的xn是当相遇时快指针已经在环上循环了x次，x>=1且为整数
=> m+y=xn => m=n-y+(x-1)*n //下面解释为什么写成这种形式

接下来将快指针置于表头(此时快指针在a处，慢指针在c处)，与慢指针以相同速度在链表上移动，当快指针移动到b处时，移动了m的距离，根据上面的等式可知，慢指针移动了n-y+(x-1)*n的距离。

我们来分析一下此时的慢指针在什么位置：
先移动(x-1)*n的距离，相当于在环上循环了(x-1)次，慢指针又回到了c点，然后再移动n-y的距离，如图所示，n-y正好是c点到b点的距离，说明此时慢指针也移动到了b点，即快慢指针在环路的开头节点相遇了。

作者：chen-hui-d
链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci/solution/kuai-man-zhi-zhen-zheng-ming-bi-jiao-yan-jin-by-ch/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class ListNode(object):
    def __int__(self,val,next=None):
        self.val=val
        self.next=next



def if_cycle(head,pos) -> str:
    if len(head)<2 or pos<0:
        return "no cycle"


class Solution(object):
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return

        slow = head
        fast = head

        # fast,slow遍历至相交或遍历完为止
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break

        # 无环链表
        if slow!=fast:
            return

        # fast从新开头遍历，相交点必为环起点
        fast = head
        while slow!=fast:
            slow=slow.next
            fast=fast.next

        return slow

