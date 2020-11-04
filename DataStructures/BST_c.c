#include<stdio.h>
#include<stdlib.h>

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
void inOrder(BST_node *root) {
    if(root != NULL) {
        inOrder(root->left);
        printf("%d", root->key);
        inOrder(root->right);
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
        return search(root->left, target)
    }

    return -1;
}