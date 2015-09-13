class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        first_unique = None
        prev = head
        node = head.next
        while node is not None:
            if prev.val != node.val:
                first_unique = node
                prev.next = first_unique
                prev = first_unique
                first_unique = None
            elif node.next is None:
                prev.next = None
                
            node = node.next
        return head

class Solution_with_test(object):
    def __init__(self, l):
        """
        :type l: list
        :rtype: ListNode
        """ 
        self.length = len(l)
        i = 1
        self.head = ListNode(l[0])
        prev = self.head
        while i < len(l):
            node = ListNode(l[i])
            prev.next = node
            prev = node
            i += 1

    def print_head(self):
        node = self.head
        while node is not None:
            print node.val, ' ',
            node = node.next
        print '\n'

    def deleteDuplicates(self, head=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head = self.head
        first_unique = None
        prev = head
        node = head.next
        while node is not None:
            if prev.val != node.val:
                prev = node
                node = node.next
            else:
                if node.next is None:
                    prev.next = None
                    node = None
                else:
                    node.val = node.next.val
                    node.next = node.next.next

        return self.head

l = [1,2,3,4,4,4,6,6,7,8,9]
l = [1,1,1]
l = [1,1,2,2]
l = [1,2,3]
s = Solution_with_test(l) 
s.print_head()
s.deleteDuplicates()
s.print_head()
