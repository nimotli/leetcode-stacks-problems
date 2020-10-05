#NAME : RANGE SUM OF BST
#CATEGORY : STACKS
#DIFFICULTY : EASY
#LINK : https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = []
        stack.append(root)
        sum = 0
        while len(stack)>0:
            current = stack.pop()
            if current.val <= R and current.val>= L:
                sum=sum+current.val
            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)
        return sum