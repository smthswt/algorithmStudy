# https://leetcode.com/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        print(s)


solution = Solution()
solution.reverseString(["h", "e", "l"])
