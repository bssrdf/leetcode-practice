class TwoSum:
    def __init__(self):
        self.nums = []

    def add(self, v):
        self.nums.append(v)

    def find(self, target):
        lookup = {}
        for i in self.nums:
            j = target - i
            if j in lookup: return True
            lookup[i] = True
        return False

if __name__ == "__main__":
    t = TwoSum()
    t.add(1); t.add(3); t.add(5)
    print t.find(4), t.find(7)

