# 442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        my_dict = {}
        res = []
        for num in nums:
            my_dict[num] = my_dict.get(num, 0)+1
        for key,val in my_dict.items():
            if val == 2:
                res.append(key)
        
        return res

obj = Solution()
ans = obj.findDuplicates([4,3,2,7,8,2,3,1])
print(ans)