class Solution:
    def read(self, buf, n):
        i = 0
        while True:
            buf4 = ['']*4
            curr = min(read4(buf4), n-i)
            for j in range(curr):
                buf[i] = buf4[j]
                i+=1
            if curr!=4 or i==n:
                return i

if __name__ == "__main__":
    s = Solution()
    content = 'abcdefghijklmnopqistuvwxyz'
    i = 0
    def read4(buf4):
        j = 0
        global i, content
        while i<len(content) and j<4:
            buf4[j] = content[i]
            j+=1; i+=1
        return j
    buf = ['']*10
    print s.read(buf, 10)
    print buf
