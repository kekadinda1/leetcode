#28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            j = 0

            while j < m and haystack[i + j] == needle[j]:
                j += 1

            if j == m:
                return i

        return -1

obj = Solution()

haystack = "sadbutsad"
needle = "sad"

result = obj.strStr(haystack, needle)

print(result)