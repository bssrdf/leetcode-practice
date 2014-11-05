class Solution:
    def jump(self, A):
        step = -1; i = 0; farthest = 0
        while i < len(A) and i <= farthest:
            next_farthest = 0
            while i < len(A) and i <=farthest:
                next_farthest = max(next_farthest, i+A[i])
                i+=1
            farthest = next_farthest
            step+=1
        return step

if __name__=="__main__":
    s = Solution()
    print s.jump([2,3,1,1,4])
