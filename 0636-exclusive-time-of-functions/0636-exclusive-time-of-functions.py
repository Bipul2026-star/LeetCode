class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack=[]
        result=[0]*n
        prev=0

        for log in logs:
            id,typ,time=log.split(":")
            id,time=int(id),int(time)

            if typ=="start":
                if stack:
                    result[stack[-1]]+=time-prev
                stack.append(id)
                prev=time
            else:
                result[stack.pop()]+=time-prev+1
                prev=time+1
        return (result)
       