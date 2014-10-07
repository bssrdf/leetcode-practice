class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0: return 0
        if len(A) == 1: return 1
        slow = 1; prev = A[0]
        for fast in range(1, len(A)):
            if A[fast] == prev:
                fast += 1
                continue
            else:
                A[slow] = A[fast]
                prev = A[fast]
                slow +=1; fast += 1
        return slow

if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([1])
    print s.removeDuplicates([1,1,2])

