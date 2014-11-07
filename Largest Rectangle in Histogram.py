class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        # keep a stack, push when the trend is increasing
        # pop only when the trend becomes decreasing
        # when the trending is decreasing, this is the right edge for some top elements in the stack
        # the left edge will be the previous element in the stack
        # boundary conditions: leftmost and rightmost bars
        increasing = []; max_area = 0; i = 0
        while i<=len(height):
            # if stack is empty or trend is increasing
            # >= or > are both OK
            if len(increasing) == 0 or (i<len(height) and height[i]>=height[increasing[-1]]):
                increasing.append(i)
                i+=1
            else:
                last = increasing.pop()
                # if stack is empty which means left edge is coordinate -1
                if len(increasing) == 0:
                    max_area = max(max_area, height[last] * (i))
                else:
                    max_area = max(max_area, height[last] * (i-increasing[-1]-1))
        return max_area

if __name__ == "__main__":
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
    print s.largestRectangleArea([2,2,2,2,2,2])
        