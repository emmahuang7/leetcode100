class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tmp = x^y
        d = 0
        while tmp:
            tmp = tmp&(tmp-1)
            d += 1
        return d
