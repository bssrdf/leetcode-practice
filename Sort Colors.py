class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        last_zero = -1; first_two = len(A); checker = 0
        while checker < first_two:
            if A[checker] == 0:
                last_zero+=1
                A[last_zero], A[checker] = 0, A[last_zero]
                checker+=1
            elif A[checker] == 2:
                first_two-=1
                A[first_two], A[checker] = 2, A[first_two]
            else: 
                checker+=1

if __name__ == "__main__":
    s = Solution()
    input = [0,1,2,0,2,1]
    s.sortColors(input)
    print input   