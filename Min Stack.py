class MinStack:
    def __init__(self):
        self.s = []
        self.m = 0

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.s) == 0:
            self.m = x
            self.s.append(0)
        else:
            self.s.append(x-self.m)
            if x<self.m: self.m = x

    # @return nothing
    def pop(self):
        if len(self.s)>0: 
            pop = self.s.pop()
            if pop<0:  self.m = self.m-pop

    # @return an integer
    def top(self):
        if len(self.s)>0:
            if self.s[-1] < 0: return self.m
            else: return self.s[-1]+self.m

    # @return an integer
    def getMin(self):
        if len(self.s)>0:
            return self.m

if __name__ == "__main__":
    s = MinStack()
    s.push(3); s.push(2); s.push(1); s.push(6)
    print s.s, s.m
    print s.top(), s.getMin()
    s.pop(); print s.top(), s.getMin()
    s.pop(); print s.top(), s.getMin()
    s.pop(); print s.top(), s.getMin()