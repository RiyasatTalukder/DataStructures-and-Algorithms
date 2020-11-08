#include<stdio.h>
#include<stdlib.h>

/*
The following is an implementation of the BST Data Structure in C.
Amortized Time complexity of the standard operations insert, search, delete: O(log(N))
Time complexity for the traversals: O(N)
*/

typedef struct BST_Node_Structure 
{
    int key;
    struct BST_Node_Structure *left;
    struct BST_Node_Structure *right;
} BST_node;

BST_node *newBSTNode(int key) {

    BST_node *new_node = NULL;
    new_node = (BST_node*)calloc(1, sizeof(BST_node));
    if (new_node != NULL) {
        new_node->key = key;
        new_node->left = NULL;
        new_node->right = NULL;
    }
    return new_node;
}
BST_node *insert(BST_node *root, BST_node *node) {
    if(root == NULL) {
        return node;
    }
    //allows for duplicate values to be inserted
    if(root->key <= node->key) {
        root->right = insert(root->right, node);
    } else {
        root->left = insert(root->left, node);
    }
    return root;
}
BST_node *findSuccessor(BST_node *root_right) {

    while(root_right->left != NULL){
        root_right = root_right->left;
    }
    return root_right;

}
BST_node *delete(BST_node *root, int key) {

    if(root == NULL) {
        return NULL;
    }
    if(root->key == key) {
        if(root->right == NULL && root->left == NULL) {
            free(root);
            return NULL;
        }
        if(root->right == NULL) {
            BST_node *temp = root->left;
            free(root);
            return temp;
        } else if (root->left == NULL) {
            BST_node *temp = root->right;
            free(root);
            return temp;
        } else {
            BST_node *successor = findSuccessor(root->right);
            root->key = successor->key;
            root->right = delete(root->right, successor->key);
            return root;
        }
    }
    if(key < root->key) {
        root->left = delete(root->left, key);

    } else { 
        root->right = delete(root->right, key);
    }
    return root;

}
void deleteBST(BST_node* root) {
    if(root != NULL){
        deleteBST(root->left);
        deleteBST(root->right);
        free(root);
    }
}
void inOrder(BST_node *root) {
    if(root != NULL) {
        inOrder(root->left);
        printf("%d", root->key);
        inOrder(root->right);
    }
}
void postOrder(BST_node *root) {
    if(root != NULL) {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d", root->key);
    }
}
void preOrder(BST_node *root) {
    if(root != NULL) {
        printf("%d", root->key);
        preOrder(root->left);
        preOrder(root->right);
    }
}
int search(BST_node *root, int target) {

    if(root == NULL) {
        return -1;
    }
    if(root->key == target) {
        return root->key;
    }
    if(root->key < target){
        return search(root->right, target);
    } else {
        return search(root->left, target);
    }
    return -1;
}
//generate BST here
int main() {
    return 0;
}