






class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return -1 if needle not in haystack else haystack.index(needle)

solution = Solution()
ans = solution.strStr('hello', 'll')
print(ans)

