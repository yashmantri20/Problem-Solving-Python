# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(node, res):
    if not node:
        return;
    traverse(node.left, res)
    res.append(node.val)
    traverse(node.right, res)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        traverse(root, res)
        return res
        
        