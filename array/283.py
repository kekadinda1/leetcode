# 283. Move zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in nums:
            if i != 0:
                nums[k] = i
                k += 1
        while k<len(nums):
            nums[k] = 0
            k += 1
        return nums
obj = Solution()
output = obj.moveZeroes([0,1,0,3,12])
print(output)
