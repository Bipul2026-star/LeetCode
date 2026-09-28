class Solution:
    def maxDepth(self, s: str) -> int:
        c_depth=0
        m_depth=0
        for ch in s:
            if ch=="(":
                c_depth+=1
                if c_depth>m_depth:
                    m_depth=c_depth
            elif ch==")":
                c_depth-=1
        return(m_depth)