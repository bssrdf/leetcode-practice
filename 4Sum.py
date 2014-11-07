class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        length = len(num); res = set(); lookup = {}
        num.sort()
        for i in range(length-1):
            for j in range(i+1, length):
                if num[i]+num[j] not in lookup:
                    lookup[num[i]+num[j]] = [(i, j)]
                else:
                    lookup[num[i]+num[j]].append((i, j))
        for i in range(length-3):
            for j in range(i+1, length-2):
                check = target - num[i] - num[j]
                if check in lookup:
                    for candidate in lookup[check]:
                        if candidate[0] > j:
                            res.add((num[i], num[j], num[candidate[0]], num[candidate[1]]))
        return [list(i) for i in res]

if __name__ == "__main__":
    s=Solution()
    print s.fourSum([1, 0, -1, 0, -2, 2], 0)


