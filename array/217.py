# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums = set()
        for i in nums:
            if i in new_nums:
                return True
            new_nums.add(i)
        return False

obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
