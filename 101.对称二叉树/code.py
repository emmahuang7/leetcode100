#思路1：递归
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left,root.right)

 
    def helper(self,pa,pb):
        if not pa and not pb:
            return True
        if not pa or not pb:
            return False
        if pa.val != pb.val:
            return False
        return self.helper(pa.left,pb.right) and self.helper(pa.right,pb.left)
#思路2：迭代
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]

        while queue:
            stack = []
            layer = []
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                stack.append(node.left)
                stack.append(node.right)
                layer.append(node.val)
            if layer != layer[::-1]:
                return False
            queue = stack
        return True
        
