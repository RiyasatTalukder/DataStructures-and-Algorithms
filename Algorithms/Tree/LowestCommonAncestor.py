'''
Given a tree and two TreeNodes, find the lowest
common ancestor of both the node's.

Time: O(N)
Space: O(1) //O(n) if we factor stack space
'''

class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    #found the node, return it to the parent
    if root.val == p.val or root.val == q.val:
        return root
    
    #continue searching for target node's
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    #if both node's are present in the subtree, return common ancestor
    if left != None and right != None:
        return root
    #if both node's are not found in the subtree, we have no ancestor
    if left == None and right == None:
        return None
    
    #if one of them is found, return it to parent and continue search
    return left if left else right

tree = TreeNode(3, TreeNode(4, TreeNode(1, None, None), TreeNode(2, None, None)), TreeNode(5, None, None))
p = TreeNode(1, None, None)
q = TreeNode(4, None, None)

assert lowest_common_ancestor(tree, p, q).val == 4