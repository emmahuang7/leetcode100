class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        # 注意helper为空时 直接入栈
        if not self.helper or x<= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        """
        :rtype: None
        """
        tmp = self.stack.pop()
        if self.helper and self.helper[-1] == tmp:
            self.helper.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None


    def getMin(self):
        """
        :rtype: int
        """
        if self.helper:
            return self.helper[-1]
        return None
