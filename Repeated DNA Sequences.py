class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        if len(s)<=10: return []
        dna = {'A':0b00, 'T':0b01, 'G':0b10, 'C':0b11}
        num = {0b00:'A', 0b01:'T', 0b10:'G', 0b11:'C'}
        current = 0b00; mask = 0b11111111111111111111
        candidates = []
        for i in range(10):
            current = ((current<<2)+dna[s[i]])&mask
        lookup = {current:False}
        for i in range(1, len(s)-9):
            current = ((current<<2)+dna[s[i+9]])&mask
            if current not in lookup: lookup[current] = False
            elif (current in lookup) and (lookup[current] == False):
                candidates.append(current); lookup[current] = True
        results = []
        for candidate in candidates:
            result = ""; mask = 0b11
            for i in range(10):
                result = num[(candidate&mask)]+result
                candidate = candidate>>2
            results.append(result)
        return results

if __name__ == "__main__":
    s = Solution()
    print s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
