'''
给定一个2n整数的数组，你的任务是将这些整数分成n对整数，例如（a 1，b 1），（a 2，b 2），...，（a n，b n）对于从1到n的所有
i ，min（a i，b i）的总和尽可能大。

输入： [1,4,3,2] 输出： 4
 说明： n是2，并且对的最大和是4 = min（1,2）+ min（3,4）。

 注意：
n是一个正整数，在[1，10000]范围内。
数组中的所有整数都在[-10000，10000]范围内。
'''

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])


a = Solution()
nums = [1,4,6,2]
solution = a.arrayPairSum(nums)
print(solution)