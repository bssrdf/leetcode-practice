class Solution:
    def canJump(self, A):
        farthest = 0
        for i in range(len(A)):
            if i > farthest: return False
            farthest = max(farthest, i+A[i])
            if farthest >= len(A)-1: return True

if __name__=="__main__":
    s = Solution()
    print s.canJump([2,3,1,1,4])
    print s.canJump([3,2,1,0,4])
