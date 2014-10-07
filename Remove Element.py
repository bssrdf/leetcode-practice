class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        front = 0; back = len(A)-1
        while front <=back:
            if A[front] == elem:
                A[front] = A[back]
                A[back] = elem
                back -= 1
            else:
                front += 1
        return back+1

if __name__ == "__main__":
    s = Solution()
    a = [3,3]
    end = s.removeElement(a, 3)
    print a[:end]

