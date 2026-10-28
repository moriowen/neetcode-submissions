# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case - if subroot and root doesn't exist 
        if not subRoot:
            return True

        if not root:
            return False

        # check if same tree
        if self.isSameTree(root, subRoot):
            return True

        # check left and right subtree with recursion 
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, root, subRoot):
        # base case - both trees are at the end of recursion and same
        if not root and not subRoot:
            return True

        # one of the two tree nodes doesn't exist  
        if not root or not subRoot:
            return False

        # val does not match 
        if root.val != subRoot.val:
            return False

        # recursive call to subtrees
        return (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right))