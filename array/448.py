# 448. Find All Numbers Disappeared in an Array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        missing_num = []
        for i in range(1,len(nums)+1):
            if i not in num_set:
                missing_num.append(i)
        return missing_num

obj = Solution()
arr = list(map(int, input().split()))
res = obj.findDisappearedNumbers(arr)
print(res)