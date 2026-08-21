# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_list = s.split()
        return len(new_list[-1])

obj = Solution()
print(obj.lengthOfLastWord("hello keka dinda "))
