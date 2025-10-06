class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        s_freq = [0] * 26
        p_freq = [0] * 26
        for i in range(len(p)):
            s_freq[ord(s[i])-ord('a')] += 1
            p_freq[ord(p[i])-ord('a')] += 1

        l = 0 
        r = len(p)-1
        res = []
        while r < len(s):
            if s_freq == p_freq:
                res.append(l) 
            s_freq[ord(s[l]) - ord('a')] -= 1
            l += 1
            if r + 1 < len(s):
                s_freq[ord(s[r+1]) - ord('a')] += 1
            r += 1
        return res
