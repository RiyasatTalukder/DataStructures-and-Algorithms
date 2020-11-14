class Node:
    key = 0
    left = None
    right = None
    balance_factor = 0

class AVLTree:
    root = None

    def search(self, root, key):
        if(key == root.key):
            return root
        if(key < root.key):
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)



