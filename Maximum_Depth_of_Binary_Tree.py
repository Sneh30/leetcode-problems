# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def solve(node):
            if node is None:
                return 0
            lh=solve(node.left)
            rh=solve(node.right)
            return 1+max(lh,rh)
        return solve(root)