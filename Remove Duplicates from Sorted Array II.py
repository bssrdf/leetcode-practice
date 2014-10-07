class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0: return 0
        if len(A) == 1: return 1
        slow = 1; prev = A[0]; cnt = 1
        for fast in range(1, len(A)):
            if A[fast] == prev:
                if cnt >= 2:
                    cnt += 1; fast += 1
                else:
                    A[slow] = A[fast]
                    cnt +=1; slow += 1; fast += 1
            else:
                A[slow] = A[fast]
                prev = A[slow]
                cnt = 1; slow +=1; fast += 1
        return slow

if __name__ == "__main__":
    s = Solution()
    a = [1,1,1,1,3,3]
    end = s.removeDuplicates(a)
    print a[:end]



