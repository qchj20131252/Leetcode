'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        for s in range(max(len(num1),len(num2))):
            if i - s < 0:
                temp = ord(num2[j - s])-ord('0') + carry
                carry = int(temp/10)
                digit = temp%10
                num.insert(0,digit)
                continue
            if j - s < 0:
                temp = ord(num1[i - s])-ord('0') + carry
                carry = int(temp/10)
                digit = temp%10
                num.insert(0,digit)
                continue
            temp = (ord(num1[i - s])-ord('0'))+(ord(num2[j - s])-ord('0')) + carry
            carry = int(temp / 10)
            digit = temp % 10
            num.insert(0, digit)
        if carry != 0:
            num.insert(0,carry)
        result = ''
        for s in num:
            result += str(s)
        return result

a =Solution()
print(a.addStrings('1','2'))