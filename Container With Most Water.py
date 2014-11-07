class Solution:
    # @return an integer
    def maxArea(self, height):
        i=0; j=len(height)-1; max_area = 0
        while i<j:
            max_area = max(max_area, (j-i)*min(height[i], height[j]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area

if __name__ == "__main__":
    s = Solution()
    print s.maxArea([1,5,2,3,1])