class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_h = {}
        t_h = {}

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in s_h:
                    s_h[s[i]] += 1
                else:
                    s_h[s[i]] = 0
                if t[i] in t_h:
                    t_h[t[i]] += 1
                else:
                    t_h[t[i]] = 0
            if s_h == t_h:
                return True

        return False