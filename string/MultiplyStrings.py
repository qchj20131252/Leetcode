'''
给定两个以字符串表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积。
注意：
num1 和 num2 的长度均小于110。
num1 和 num2 均只包含数字 0-9。
num1 和 num2 均不以零开头。
你不能使用任何内置的大整数库或直接将输入转换为整数。
'''

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num = []
        for i in range(len(num1)+len(num2)):
            num.append(0)
        i = len(num1) - 1
        while i >= 0:
            j = len(num2) - 1
            while j >= 0:
                num[i+j+1] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                j -= 1
            i -= 1

        carry = 0
        k = len(num1) + len(num2) - 1
        while k >= 0:
            num[k] += carry
            carry = int(num[k]/10)
            num[k] =num[k]%10
            k -= 1
        result = ''
        firstNonZero = True
        for s in num:
            if firstNonZero and s == 0:
                continue
            else:
                result += str(s)
                firstNonZero = False
        return result



a = Solution()
print(a.multiply("123","456"))
