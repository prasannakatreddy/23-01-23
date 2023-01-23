class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        c = 1
        m = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    c += 1
                else:
                    break
            m = c if c>m else m
            c = 1
        return m
