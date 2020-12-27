class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    if(root == None):
        return 0
    path = 0
    def depth(root):
        if(root == None):
            return 0
        leftDepth = depth(root.left)
        rightDepth = depth(root.right)
        path = max(path, leftDepth+rightDepth)
        
        return 1+max(leftDepth, rightDepth)
    
    depth(root)
    return path