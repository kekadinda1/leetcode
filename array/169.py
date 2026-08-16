# 169. Majority element

class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


obj = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
result = obj.majorityElement(nums)
print("Majority Element:", result)