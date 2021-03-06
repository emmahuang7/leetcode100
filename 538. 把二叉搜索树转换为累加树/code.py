
# 反向中序 非递归
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node = root
        stack = []
        tmp = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            if stack:
                node = stack.pop()
                tmp += node.val
                node.val = tmp
                node = node.left
        return root

#反向中序 递归
class Solution(object):
    def __init__(self):
        self.sum_ = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 0
        self.convertBST(root.right)
        self.sum_ += root.val
        root.val = self.sum_
        self.convertBST(root.left)
        return root
