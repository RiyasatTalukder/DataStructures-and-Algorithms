class Node:
    key = 0
    parent = None
    left = None
    right = None
    balance_factor = 0

class AVLTree:
    root = Node
    def search(self, root, key):
        if(key == root.key):
            return root
        if(key < root.key):
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    
    def leftRotate(self, root):
        #left subtree of pivot becomes right subtree of root, pivot becomes new root

        #make right subtree of root = left subtree of pivot
        pivot = root.right
        root.right = pivot.left
        #re-assign the parents accordingly
        if(pivot.left != None):
            pivot.left.parent = root
        pivot.parent = root.parent
        if(root.parent == None):
            self.root = pivot
        elif(root.parent.left == root):
            root.parent.left = pivot
        else:
            root.parent.right = pivot

        pivot.left = root
        root.parent = pivot
        #update balance factors
        
        return pivot
    
    def rightRotate(self, root):
        #right rotation is symmetric to left rotation
        pivot = root.left
        root.left = pivot.right
        #re-assign the parents accordingly
        if(pivot.right != None):
            pivot.right.parent = root
        pivot.parent = root.parent
        if(root.parent == None):
            self.root = pivot
        elif(root.parent.right == root):
            root.parent.right = pivot
        else:
            root.parent.left = pivot

        pivot.right = root
        root.parent = pivot
        #update balance factors
        
        return pivot

        





