class Solution:
    # @return a string
    def intToRoman(self, num):
        numeral_map = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        keys = sorted(numeral_map.keys()); result = ''
        while num!=0:
            for i in reversed(range(len(keys))):
                if num/keys[i]>=1:
                    result = result+numeral_map[keys[i]]*(num/keys[i])
                    num = num%keys[i]
        return result

if __name__ == "__main__":
    s = Solution()
    print s.intToRoman(1986)
