# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def iterator(l_nodes: list, r_nodes: list):
            temp_l, temp_r = [], []
            l_vals, r_vals = "", ""
            for node in l_nodes:
                if node.left:
                    temp_l.append(node.left)
                    l_vals += str(node.left.val)
                if node.right:
                    temp_l.append(node.right)
                    r_vals += str(node.right.val)
            for node in r_nodes:
                if node.right:
                    temp_l.append(node.right)
                    r_vals += str(node.right.val)
                if node.left:
                    temp_l.append(node.left)
                    l_vals += str(node.left.val)
            if len(l_vals) == 0 and len(r_vals) == 0:
                output = True
            elif l_vals == r_vals:
                output = iterator(temp_l, temp_r)
            else:
                output = False

            return output

        if not root.left and not root.right:
            return True
        elif root.left and root.right and root.left.val != root.right.val:
            return False

        return iterator([root.left], [root.right])

s = Solution()
print(s.isSymmetric())