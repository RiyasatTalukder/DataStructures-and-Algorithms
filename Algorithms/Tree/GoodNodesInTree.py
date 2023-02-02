'''
Given a binary tree root, a node X in the tree is named good if 
in the path from root to X there are no nodes with a value greater than X.

Time: O(n)
Space: O(1)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def goodNodes(root):
    count = [0]
    def traverse(root, max_val_path):
        if not root:
            return

        max_val_path = max(max_val_path, root.val)
        if root.val >= max_val_path:
            count[0] += 1

        traverse(root.left, max_val_path)
        traverse(root.right, max_val_path)
    
    traverse(root, root.val)
    return count[0]

root = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
assert goodNodes(root) == 3

