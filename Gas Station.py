class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        i = 0; tank = 0; start = 0; total = 0
        while i < len(gas):
            diff = gas[i]-cost[i]
            if tank+diff<0:
                tank=0
                start=i+1
            else:
                tank+=diff
            i+=1
            total+=diff
        if total>=0: return start
        return -1
        
if __name__ == "__main__":
    s = Solution()
    print s.canCompleteCircuit([2, 2], [3, 1])
    print s.canCompleteCircuit([1, 2], [3, 2])


