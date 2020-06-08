class Solution(object):
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.height(root)
        return self.max

    def height(self,root):
        if not root:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        self.max = max(self.max,l+r)
        return 1+max(l,r)
