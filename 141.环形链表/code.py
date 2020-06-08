class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
          return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return True
