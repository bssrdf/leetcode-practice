import sys

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        i = 0; res = 0; closest_diff = 9223372036854775807
        while i < len(num)-2:
            j = i+1; k=len(num)-1
            while j<k:
                diff = num[i]+num[j]+num[k]-target
                if diff<0:
                    if abs(diff) < abs(closest_diff):
                        closest_diff = diff
                    j+=1
                elif diff > 0:
                    if abs(diff) < abs(closest_diff):
                        closest_diff = diff
                    k-=1
                else:
                    return target
            i+=1
        return closest_diff+target

if __name__ == "__main__":
    s = Solution()
    print s.threeSumClosest([-1,2,1,-4], 1) 


