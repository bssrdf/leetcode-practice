class Solution:
    def __init__(self):
        self.buf_size, self.offset = 0, 0
        self.buf4 = ['']*4

    def read(self, buf, n):
        i = 0; eof = False
        while((not eof) and (i<n)):
            sz = self.buf_size if self.buf_size>0 else read4(self.buf4)
            if (self.buf_size == 0) and sz<4: eof = True
            curr = min(sz, n-i)
            for j in range(curr):
                buf[i] = self.buf4[self.offset+j]
                i += 1
            self.buf_size = sz-curr
            self.offset = (self.offset+curr)%4
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
    buf = ['']*10
    print s.read(buf, 10)
    print buf
    buf = ['']*10
    print s.read(buf, 10)
    print buf