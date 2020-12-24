class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(s, t):
    """
    Given 2 binary trees, the algorithm checks if t is 
    a subtree of s. It returns true if it is, false otherwise.

    Time: O(n*m)
    Space: O(min(n,m))
    """

    #helper function that checks if the trees at some level are same
    def isSameTree(s, t):
        #if we reached the end of the tree, they must be the same if t is subtree
        if(s == None or t == None):
            return s == t
        #if the root is the same, we check if the left and right subtrees of the root are also the same
        if(s.val == t.val):
            return isSameTree(s.right, t.right) and isSameTree(s.left, t.left)
    
    #Approach: we will check if t is a subtree of s at each level of s
    if(s == None):
        #reached end of tree and did not find t
        return False
    #if same tree, return true
    if(isSameTree(s, t)):
        return True
    #if its not the same, move one level down and check again
    else:
        return isSubtree(s.left, t) or isSubtree(s.right, t)

s = TreeNode(3, TreeNode(4, TreeNode(1, None, None), TreeNode(2, None, None)), TreeNode(5))
t = TreeNode(4, TreeNode(1, None, None), TreeNode(2, None, None))
assert True == isSubtree(s, t)