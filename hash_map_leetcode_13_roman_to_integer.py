class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
                result -= dic[s[i]]
            else:
                result += dic[s[i]]
        return result
if __name__ == '__main__':
    s = "MCMXCIV"
    a = Solution().romanToInt(s)
    print(a)