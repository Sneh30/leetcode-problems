# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl=head
        fa=head
        while fa is not None and fa.next is not None:
            sl=sl.next
            fa=fa.next.next
            if sl==fa:
                return True
        return False
