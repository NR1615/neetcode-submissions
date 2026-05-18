class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos=0

        for ch in s:
            found=False

            for j in range(pos, len(t)):
                if ch==t[j]:
                    pos=j+1
                    found=True
                    break
            if not found:
                return False
        return True