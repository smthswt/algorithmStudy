# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # 1-indexed
            elif total < target:
                left += 1
            else:
                right -= 1


numbers = [2,7,11,15]
target = 9

solution = Solution()
print(solution.twoSum(numbers, target))