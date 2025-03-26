# https://leetcode.com/problems/merge-sorted-array/description/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1  # nums1 실제 값의 마지막 인덱스
        p2 = n - 1  # nums2 마지막 인덱스
        p = m + n - 1  # nums1 전체 마지막 인덱스 (결과 채울 위치)

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # nums2에 남은 게 있으면 복사 (nums1은 이미 제자리에 있음)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)
