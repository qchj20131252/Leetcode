class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        temp = []
        result = []
        for array in nums:
            for num in array:
                temp.append(num)
        if r*c != len(temp):
            return nums
        for i in range(r):
            result.append(temp[i*c:(i+1)*c])
        return result


nums = [[1,2],[3,4]]
example = Solution()
print(example.matrixReshape2(nums,1,4))