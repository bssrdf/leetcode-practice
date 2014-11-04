class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) == 1: return num
        i = len(num)-2
        while i>=0:
            if num[i] < num[i+1]: break
            else: i-=1
        if i==-1: return list(reversed(num))
        first = num[i]
        j = len(num)-1
        while j>i:
            if num[j] > first: break
            else: j-=1
        num[i], num[j] = num[j], num[i]
        return num[:i+1]+list(reversed(num[i+1:]))    
        
if __name__ == "__main__":
    s = Solution()
    print s.nextPermutation([1,2,3,4,8,7,6,5])    


