class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashs[s[i]] = 1 + hashs.get(s[i], 0)
            hasht[t[i]] = 1 + hasht.get(t[i], 0)    # key is t[i], not s[i]

        for c in hashs:
            if hashs[c] != hasht.get(c, 0):          # .get avoids KeyError
                return False
        return True