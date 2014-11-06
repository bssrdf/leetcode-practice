class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 0: return num[0]
        start = 0; end = len(num)-1
        while start<=end:
            if num[start] == num[end]:
                start+=1
            elif num[start] < num[end]:
                return num[start]
            else: # num[start] > num[end]
                mid = (start+end)/2
                if num[mid] >= num[start]:
                    start = mid+1
                else:
                    end = mid
        return num[end]

if __name__ == "__main__":
    s = Solution()
    print s.findMin([4,5,6,7,0,1,2,3,4])
    print s.findMin([4,5,6,7,8,0,1,2,3,4])
    print s.findMin([3,1,2,3])
    print s.findMin([2,1,2])
    print s.findMin([1])
