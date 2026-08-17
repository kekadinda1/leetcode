# 219 Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for i in range(0,len(nums)):
            if nums[i] in my_dict:
                if i - my_dict[nums[i]] <= k:
                    return True
            
            my_dict[nums[i]] = i
        return False


obj = Solution()
print(obj.containsNearbyDuplicate([1,2,3,1],3))
print(obj.containsNearbyDuplicate([1,2,3,1,2,3],2))
