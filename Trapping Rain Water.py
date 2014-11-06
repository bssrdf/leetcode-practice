class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left_maxes = [0 for i in range(len(A))]
        right_maxes = [0 for i in range(len(A))]
        left_max, right_max = 0, 0
        water = [0 for i in range(len(A))]
        for i in range(len(A)):
            left_maxes[i] = left_max
            left_max = max(left_max, A[i])
        for i in reversed(range(len(A))):
            right_maxes[i] = right_max
            right_max = max(right_max, A[i])
        for i in range(len(A)):
            if A[i]<left_maxes[i] and A[i]<right_maxes[i]:
                water[i] = min(left_maxes[i], right_maxes[i])-A[i]
        return sum(water)

if __name__ == "__main__":
    s = Solution()
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
