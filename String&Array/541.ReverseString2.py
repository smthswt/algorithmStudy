# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # 문자열은 변경 불가능하니까 리스트로 변환
        for i in range(0, len(s), 2 * k):
            # i부터 i+k 전까지 뒤집기
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)  # 다시 문자열로 합쳐서 반환


solution = Solution()
print(solution.reverseStr("abcde", 2))