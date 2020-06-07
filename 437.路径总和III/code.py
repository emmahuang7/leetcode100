#思路1：双重递归
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.path(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
    def path(self,root,sum):
        if not root:
            return 0
        count = 0
        if root.val == sum:
            count += 1
        count += self.path(root.left,sum-root.val)
        count += self.path(root.right,sum-root.val)
        return count

#思路2：前缀树
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.count = 0
        preSum = 0
        prefixTree = {0:1}
        self.dfs(root,sum,preSum,prefixTree)
        return self.count
    
    def dfs(self,root,sum,preSum,prefixTree):
        if not root:
            return 0 
        preSum += root.val
        oldSum = preSum-sum
        if oldSum in prefixTree:
        #不是加1 
            self.count += prefixTree[oldSum]
        prefixTree[preSum] = prefixTree.get(preSum,0)+1
        self.dfs(root.left,sum,preSum,prefixTree)
        self.dfs(root.right,sum,preSum,prefixTree)
        #返回上一层递归，需要重置状态
        prefixTree[preSum] -= 1
