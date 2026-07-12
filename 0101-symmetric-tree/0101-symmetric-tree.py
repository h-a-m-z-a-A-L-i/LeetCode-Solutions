# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            if left is None and right is None:
                return True
            if left is None and right is not None or left is not None and right is None:
                return False
            if left.val == right.val:
                return mirror(left.left, right.right) and mirror(left.right, right.left)
            return False
        if not root:
            return True
        return mirror(root.left, root.right)
            
