class MinStack(object):

    def __init__(self):
        self.st = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        min_val = self.getMin()

        if min_val == None or min_val > value:
            min_val = value

        self.st.append([value, min_val])

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1][0] if self.st else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.st[-1][1] if self.st else None