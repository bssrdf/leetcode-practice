class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if len(height)==1: return height[0]
        left_maxes = [0 for i in range(len(height))]
        right_maxes = [0 for i in range(len(height))]
        left_max = height[0]; right_max = height[-1]
        for i in range(1, len(height)):
            if height