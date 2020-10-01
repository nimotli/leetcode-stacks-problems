#NAME : BINARY TREE INORDER TRAVERSAL
#CATEGORY : STACKS
#DIFFICULTY : MEDIUM
#LINK : https://leetcode.com/problems/binary-tree-inorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root) :
        res =[]
        self.recFunc(root,res)
        return res
        
    def recFunc(self,root,res):
        if root is not None:
            if root.left is not None:
                self.recFunc(root.left,res)
            res.append(root.val)
            if root.right is not None:
                self.recFunc(root.right,res)
