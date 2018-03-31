'''
反转字符串

输入：s = "hello"
返回："olleh"
'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        newS = ''
        for element in s:
            newS = element + newS
        return  newS

    def bestReverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return  s[::-1]

a = Solution()
print(a.reverseString("hello"))