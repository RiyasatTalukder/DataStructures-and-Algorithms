#linked list node definition
class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next
def mergeKLists(lists):
    """
    Given an array (length k) of sorted linked lists, the algorithm
    merges all the linked lists and returns a final sorted
    linked list. 

    Time: O(nlogk)
    Space: O(nlogk)
    """
    if(lists == []):
        return None
    
    #method that takes 2 sorted linked lists and merges them
    def merge(a, b):
        head = ListNode(-1)
        curr = head
        while(a != None and b != None):
            if(a.val <= b.val):
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next
        
        while(a != None):
            curr.next = a
            a = a.next
            curr = curr.next
        
        while(b != None):
            curr.next = b
            b = b.next
            curr = curr.next
        
        return head.next
    
    #recursively dvides the array and merges the sub linked lists
    def divide(lists, start, end):
        if(start == end):
            return lists[start]
        
        mid = (start+end)//2
        left = divide(lists, start, mid)
        right = divide(lists, mid+1, end)
        return merge(left, right)
    #return the final merged linked list
    return divide(lists, 0, len(lists)-1)


A = [ListNode(1, ListNode(2, ListNode(3))),
 ListNode(-1, ListNode(4, ListNode(10))), 
 ListNode(10, ListNode(10, ListNode(30)))]

output = mergeKLists(A)
merged = []
while(output != None):
    merged.append(output.val)
    output = output.next
assert [-1,1,2,3,4,10,10,10,30] == merged

