class Solution:
    def minOperations(self, s: str) -> int:
        if s== "".join(sorted(s)):
            return 0
        elif len(s)==2:
            return -1

        elif min(s)==s[0] or max(s)==s[-1]:
            return 1
        elif max(s)==s[0] and min(s)==s[-1]:
            if s.count(max(s))>1 or s.count(min(s))>1:
                return 2
            return 3
        else:
            return 2