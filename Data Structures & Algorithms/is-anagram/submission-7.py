class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_h = {}
        t_h = {}

        if len(s) == len(t):
            for i in range(len(s)):
                s_h[s[i]] = 1 + s_h.get(s[i], 0)
                t_h[t[i]] = 1 + t_h.get(t[i], 0)

            return s_h == t_h

        return False