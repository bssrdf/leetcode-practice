class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, nums):
        longest, lookup = 0, {num:False for num in nums}
        for num in nums:
            if lookup[num]==False:
                lookup[num] = True
                consecutive = 1; i = num-1; j=num+1
                while i in lookup and lookup[i]==False:
                    lookup[i] = True
                    consecutive+=1
                    i-=1
                while j in lookup and lookup[j]==False:
                    lookup[j] = True
                    consecutive+=1
                    j+=1
                longest = max(longest, consecutive)
        return longest

if __name__ == "__main__":
    s=Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])
    a = range(-999, 9001)
    print s.longestConsecutive(a)

