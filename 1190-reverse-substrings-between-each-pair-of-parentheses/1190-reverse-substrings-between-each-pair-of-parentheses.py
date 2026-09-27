class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        result=list(s)
        for i, ch in enumerate(s):
            if ch=="(":
                stack.append(i)
            elif ch==")":
                start=stack.pop()
                result[start:i+1]=result[start:i+1][::-1]
        return("".join(ch for ch in result if ch not in "()"))        