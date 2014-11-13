class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ways = [[0 for j in range(len(S)+1)] for i in range(len(T)+1)]
        for j in range(len(S)+1): ways[0][j] = 1
        for i in range(1, len(T)+1):
            for j in range(1, len(S)+1):
                ways[i][j] = ways[i][j-1]
                if S[j-1]==T[i-1]: ways[i][j]+=ways[i-1][j-1]
        return ways[len(T)][len(S)]

if __name__ == "__main__":
    s = Solution()
    print s.numDistinct("rabbbit", "rabbit")
    print s.numDistinct("rabbbit", "")