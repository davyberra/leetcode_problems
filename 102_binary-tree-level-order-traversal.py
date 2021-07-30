class Solution:
    def levelOrder(self, root):
        q = []
        result = []
        if root:
            result.append([root.val])
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

        node = q[0]
        while True:
            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            q.remove(node)
            if len(q) == 0:
                break
            node = q[0]

        return result


