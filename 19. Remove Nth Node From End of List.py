class Solution:
    def removeNthFromEnd(self, h, n):
        d=ListNode(0,h); f=s=d
        for _ in range(n+1): f=f.next
        while f: f=f.next; s=s.next
        s.next=s.next.next
        return d.next