#ifndef BINARY_TREE_H
#define BINARY_TREE_H

#include <iostream>

template <typename T>
class BinaryTree {
private:
    struct TreeNode {
        T data;
        TreeNode* left;
        TreeNode* right;
        TreeNode(T val) : data(val), left(nullptr), right(nullptr) {}
    };
    TreeNode* root;

    void insertInorder(TreeNode*& node, T val) {
        if (node == nullptr) {
            node = new TreeNode(val);
        } else if (val < node->data) {
            insertInorder(node->left, val);
        } else {
            insertInorder(node->right, val);
        }
    }

    void displayInorder(TreeNode* node) const {
        if (node != nullptr) {
            displayInorder(node->left);
            std::cout << node->data << " ";
            displayInorder(node->right);
        }
    }

    void destroyTree(TreeNode* node) {
        if (node != nullptr) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }

public:
    BinaryTree() : root(nullptr) {}
    ~BinaryTree() { destroyTree(root); }

    void insert(T val) { insertInorder(root, val); }
    void display() const { displayInorder(root); std::cout << "\n"; }
};

#endif