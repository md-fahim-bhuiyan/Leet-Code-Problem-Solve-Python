import heapq
class Solution:
    def mergeKLists(self, lists):
        h=[]
        for i,n in enumerate(lists):
            if n: heapq.heappush(h,(n.val,i,n))
        head=cur=ListNode(0)
        while h:
            v,i,n=heapq.heappop(h)
            cur.next=n; cur=cur.next
            if n.next: heapq.heappush(h,(n.next.val,i,n.next))
        return head.next
