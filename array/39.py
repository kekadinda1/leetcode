# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        new_list = []

        def solve(start, target, current):
            if target == 0:
                new_list.append(current.copy())
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                current.append(num)

                solve(i, target - num, current)

                current.pop()

        solve(0, target, [])

        return new_list

obj = Solution()
print(obj.combinationSum([2,3,6,7], 7))