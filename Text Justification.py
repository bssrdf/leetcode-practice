class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        results = []; i = 0
        while i < len(words):
            size = L; line = []; res = ""
            while i < len(words) and (len(words[i])+len(line))<=size:
                line.append(words[i])
                size -= len(words[i])
                i+=1
            if len(line)>1 and i!=len(words):
                space = size/(len(line)-1)
                extra = size%(len(line)-1)
                for j in range(len(line)-1):
                    res+=line[j]; res+=" "*space
                    if extra>0: res+=" "; extra-=1
                res+=line[-1]
                results.append(res)
            elif len(line)==1:
                res+=line[0]; res+=" "*size
                results.append(res)
            else:
                for j in range(len(line)-1):
                    res+=line[j]; res+=" "; size-=1
                res+=line[-1]; res+= " "*size
                results.append(res)
        return results

if __name__ == "__main__":
    s = Solution()
    res = s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    for i in res:
        print i
    res = s.fullJustify(["What","must","be","shall","be."], 12)
    for i in res:
        print i
