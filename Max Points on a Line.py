class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        result = 0
        for i in range(len(points)):
            same = 1; inf = 0; mp = {}; 
            for j in range(i+1, len(points)):
                if points[j].x == points[i].x and points[j].y == points[i].y :
                    same += 1
                elif points[j].x == points[i].x:
                    inf += 1
                else:
                    slope = (points[j].y-points[i].y)*1.0/(points[j].x-points[i].x)
                    if slope not in mp: mp[slope] = 1
                    else: mp[slope] = mp[slope]+1
            current_max = 0
            for slope in mp:
                current_max = max(mp[slope]+same, current_max)
            current_max = max(current_max, inf + same)
            result = max(current_max, result)
        return result

if __name__ == "__main__":
    s = Solution()
    class Point:
        def __init__(self, a=0, b=0):
            self.x = a
            self.y = b
    p1, p2, p3, p4 = Point(0,0), Point(0,1), Point(1,1), Point(2,2)
    points = [p1,p2,p3,p4]
    print s.maxPoints(points)

