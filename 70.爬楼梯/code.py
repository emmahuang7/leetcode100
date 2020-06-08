class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<= 2:
            return n
        a,b = 1,2
        while n-2>0:
            a,b = b,a+b
            n -= 1
        return b
