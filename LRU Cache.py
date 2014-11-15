import collections

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.size = capacity

    # @return an integer
    def get(self, key):
        if key in self.cache: 
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value            
            return value
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache: 
            del self.cache[key]
            self.cache[key] = value
        else:
            if len(self.cache) == self.size: self.cache.popitem(False)
            self.cache[key] = value

if __name__ == "__main__":
    c = LRUCache(3)
    c.set(1, 11)
    c.set(2, 22)
    c.set(3, 33)
    c.set(4, 44)
    c.get(2)
    print c.cache

