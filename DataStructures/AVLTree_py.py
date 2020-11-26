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
    
    def insert(self, root, node):
        """
        There are 4 cases for rotaion:
        - Parent refers to the grandparent of the inserted node
        - Child refers to the parent of the inserted node

        1) left-left
            In this case, the left side of the parent and its child is heavy
            We can perform a RIGHT rotation on the parent node to balance the tree

        2) left-right
            Left side of the parent is heavy and the right side of the child is heavy
            We can perform a LEFT rotation on the child and then RIGHT rotation on parent 

        3) right-right
            The right side of the parent and its child is heavy 
            We can perform a LEFT rotation on the parent node to balance the tree

        4) right-left
            The right of the parent is heavy and the left side of the child is heavy
            We can perform a RIGHT rotation on the child and then LEFT rotation on parent

        """
        #To do
        if(root == None):
            return node
        if(root.value < node.value):
            root = self.insert(root.right, node)
        else:
            root = self.insert(root.left, node)
        
        node.bf = 0
        
        return root

    def delete(self, root, node):
        """
        The cases for updating the balance factor is the same cases 
        as mentioned in the insert method
        """
        #To do
        if(root.key == None):
            return None
        if(root.key == node.key):
            if(root.left == None and root.right == None):
                root = None
            elif(root.left == None):
                temp = root.right
                temp.parent = root.parent
                root = None
                return temp
            elif(root.right == None):
                temp = root.left
                temp.parent = root.parent
                root = None
                return temp
            else:
                temp = findSuccessor(root.right)
                root.key = temp.key
                root.right = delete(temp)
                return root
                
        if(root.key < node.key):
            root.right = delete(root.right, node)
        else:
            root.left = delete(root.left, node)
        
        return root
    
    def findSuccessor(self, root):
        while(root.left != None):
            root = root.left
        return root

    def printPreOrder(self, root):
        if(root != None):
            print(root.key)
            self.printInOrder(root.left)
            self.printInOrder(root.right)

    def printInOrder(self, root):
        if(root != None):
            self.printInOrder(root.left)
            print(root.key)
            self.printInOrder(root.right)

    def printPostOrder(self, root):
        if(root != None):
            self.printInOrder(root.left)
            self.printInOrder(root.right)
            print(root.key)
    
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

        





