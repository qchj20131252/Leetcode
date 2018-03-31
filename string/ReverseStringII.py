'''
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余
的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:
该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内
'''

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for pos in range(0,len(s),k):
            if (pos/k)%2 != 0:
                temp = s[pos-k:pos][::-1]
                s = s.replace(s[pos - k:pos], str(temp))
            else:
                if pos+k >= len(s):
                    temp = s[pos:len(s)][::-1]
                    s = s.replace(s[pos:len(s)], str(temp))
        return s

a = Solution()
s = a.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",39)
ss = "abc"
print(s)
print(len("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"))
print(len("imjkfnqcqnajmebeddqsgl"))
