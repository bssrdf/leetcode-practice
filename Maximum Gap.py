class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num)<2: return 0
        maxLength = len(str(max(num)))
        strNum = [str(i)[::-1] for i in num]
        for i in range(maxLength):
            buckets = [[] for j in range(10)]
            for k in strNum:
                if len(k)<=i:
                    buckets[0].append(k)
                else:
                    buckets[int(k[i])].append(k)
            strNum = []
            for j in range(10):
                strNum.extend(buckets[j])
        num = [int(i[::-1]) for i in strNum]
        maxGap = 0
        for i in range(1, len(num)):
            maxGap = max(maxGap, num[i]-num[i-1])
        return maxGap

if __name__ == "__main__":
    s = Solution()
    print s.maximumGap([1,3,5,7,11])
