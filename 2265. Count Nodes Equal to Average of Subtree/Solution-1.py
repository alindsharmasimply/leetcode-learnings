# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root: TreeNode) -> tuple(int, int):
            nonlocal ans
            if not root:
                return (0, 0)
            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)
            summ = root.val + left_sum + right_sum
            count = 1 + left_count + right_count
            if summ // count == root.val:
                ans += 1
            return (summ, count)

        dfs(root)
        return ans
