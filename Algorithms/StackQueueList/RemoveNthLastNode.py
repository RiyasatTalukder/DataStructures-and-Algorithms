"""
Given a linked list, the algorithm removes the
nth last node from the list.

Time: O(n)
Space: O(1)
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head
    fast = slow = dummy
    
    #move fast to the position nth position
    for _ in range(n+1):
        fast = fast.next
    
    #when fast reaches the end, slow will be at the right position for removal
    while(fast != None):
        fast = fast.next
        slow = slow.next
    #remove the node
    slow.next = slow.next.next
    
    return dummy.next

test = removeNthFromEnd(ListNode(1,ListNode(2, ListNode(3))), 2)
vals = []
while(test != None):
    vals.append(test.val)
    test = test.next
assert vals == [1,3]