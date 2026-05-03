# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #check if current node is null
        if root == None: return 

        #switch left and right
        temp = root.left
        root.left = root.right
        root.right = temp

        #recursively call on left and right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root