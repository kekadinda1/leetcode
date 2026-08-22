# 409. Longest Palindrome
class Solution:
    def longestPalindrome(self, s:str)->int:
        freq = dict()
        for i in s:
            freq[i] = freq.get(i,0)+1

        res = 0
        has_odd = False
        for i in freq.values():
            if i%2 == 0:
                res += i
            else:
                res += i-1
                has_odd = True
        if has_odd:
            res += 1

        return res

obj = Solution()
ans = obj.longestPalindrome("abccccdd")
print(ans)